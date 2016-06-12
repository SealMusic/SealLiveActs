# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.seal.live.acts.1'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Seal Live Acts", "channel/UC1RzK2_Ebk8bQ5A9H2PiT0g", 'https://yt3.ggpht.com/-wEyiIoSuC4s/AAAAAAAAAAI/AAAAAAAAAAA/3OfuYRXNO2U/s88-c-k-no-rj-c0xffffff/photo.jpg'),
        ("National Live Acts", "playlist/PLvD9-mRSTbHZghAOFEnjHMhOF3Sum33vt", 'https://yt3.ggpht.com/-wEyiIoSuC4s/AAAAAAAAAAI/AAAAAAAAAAA/3OfuYRXNO2U/s88-c-k-no-rj-c0xffffff/photo.jpg'),
        ("International Live Acts", "playlist/PLvD9-mRSTbHY05jsahTVIWbewcvXysUmy", 'https://yt3.ggpht.com/-wEyiIoSuC4s/AAAAAAAAAAI/AAAAAAAAAAA/3OfuYRXNO2U/s88-c-k-no-rj-c0xffffff/photo.jpg'),				
]



# Entry point
def run():
    plugintools.log("seal.live.acts.1.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("seal.live.acts.1.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()