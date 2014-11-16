#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2
import xbmcplugin, xbmcgui, xbmc
import CommonFunctions
import xbmcaddon

import os
import subprocess

common = CommonFunctions
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name') 

#--------------------------------------------------------------------------------------------
def addDir(name,url,mode,iconimage):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok
#--------------------------------------------------------------------------------------------	
def addLink(name,url,iconimage):
    ok=True
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
    return ok
#--------------------------------------------------------------------------------------------	
def hauptmenue():
    addDir("Fritzbox", '/hauptprogramme/', 1, "")	
    addDir("Lokalfernsehen", '/lokalfernsehen/', 2, "")	
#--------------------------------------------------------------------------------------------	
def IsFritzboxPresent():
	def IsAddrPingable(address):
		import socket
		#create an INET, STREAMing socket
		s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
		#now connect to the web server on port 80
		# - the normal http port
		
		try:
			s.connect((address, 80))
			result = True
		except: # if failed to connect
			result = False
		return result		
	
	return IsAddrPingable("fritz.box")
#--------------------------------------------------------------------------------------------	
#--------------------------------------------------------------------------------------------	
params = common.getParameters(sys.argv[2])

try:
    mode = int(params['mode'])
except:
    mode = None
#--------------------------------------------------------------------------------------------
try:
    name = params['name']
except:
    name = None
#--------------------------------------------------------------------------------------------	
try:
    url = params['url']
except:
    url = None
#--------------------------------------------------------------------------------------------
# Hauptprogramm	
if mode == None:
        hauptmenue()
elif mode == 1:    
	if IsFritzboxPresent():		
		xbmcgui.Dialog().notification("fritz.box", "present", xbmcgui.NOTIFICATION_INFO)			
	else:		
		xbmcgui.Dialog().notification("fritz.box", "absent", xbmcgui.NOTIFICATION_INFO)
elif mode == 2: 
	mode = None
#--------------------------------------------------------------------------------------------		
xbmcplugin.endOfDirectory(int(sys.argv[1]))