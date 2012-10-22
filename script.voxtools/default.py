#script.voxtools

import xbmc,  xbmcgui, sys, re, StorageServer
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xbmc import getCondVisibility, getInfoLabel


def getcurrentvolas_string():
    volume_query = '{"jsonrpc": "2.0", "method": "Application.GetProperties", "params": { "properties": [ "volume" ] }, "id": 1}'
    result = xbmc.executeJSONRPC( volume_query )
    match = re.search( '"volume": ?([0-9]{1,3})', result )
    return match.group(1)
    
def getcurrentvolas_int():
    volume_query = '{"jsonrpc": "2.0", "method": "Application.GetProperties", "params": { "properties": [ "volume" ] }, "id": 1}'
    result = xbmc.executeJSONRPC( volume_query )
    match = re.search( '"volume": ?([0-9]{1,3})', result )
    intvol = int(match.group(1))
    return intvol

def mysetvol(strvol):
    targetvol = int(strvol)
    myvol = getcurrentvolas_int()   
    delta=4
    if (myvol<targetvol):
        while (myvol < targetvol-delta):
            myvol = myvol + delta
            tmpvol = str(myvol)
            xbmc.executebuiltin("SetVolume("+tmpvol+")")
            #time.sleep(0.05)
            xbmc.sleep(50)
    else:
        while (myvol > targetvol+delta):
            myvol = myvol - delta
            tmpvol = str(myvol)
            xbmc.executebuiltin("SetVolume("+tmpvol+")")
            #time.sleep(0.05)
            xbmc.sleep(50)
    xbmc.executebuiltin("SetVolume("+strvol+")")

def storeVal(strName,strVal):
    cache = StorageServer.StorageServer("VoxTools", 1) # (Your plugin name, Cache time in hours)
    cache.table_name = "VoxTools"
    cache.set(strName,strVal) 

cmdtype = sys.argv[1].split("=", 1)[1].lower()
cmdparm1 = sys.argv[2].split("=", 1)[1]
#xbmcgui.Dialog().ok("a"+"B",cmdtype+"  :  "+cmdparm1)

if cmdtype == "youtube.search":
    xbmc.executebuiltin("XBMC.ActivateWindow(10025,plugin://plugin.video.youtube/?path=/root/search&feed=search&search="+cmdparm1+"&)")
elif cmdtype == "execbuiltin":
    xbmc.executebuiltin(cmdparm1)
elif cmdtype == "setvol":    
    mysetvol(cmdparm1)
    #storeVal("volume",cmdparm1)
    
        
    
    #xbmcgui.Dialog().ok("Current Volume",cmdparm1)

    
#xbmc.getInfoLabel('Player.Volume')
#    youtubesearch(sys.argv[2])
#elif strActionType == "grooveshark":    
#    xbmc.executebuiltin("XBMC.ActivateWindow(10502,plugin://plugin.audio.groove/?mode=11&name=the Beatles&id=7587&)")




    
#	xbmcgui.Dialog().ok("Error","no search term specified")

