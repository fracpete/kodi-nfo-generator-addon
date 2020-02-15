import xbmcaddon
import xbmcgui
import subprocess

addon     = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

cmd = [
    "kodi-nfo-gen", 
    "--dir",
    "/media/xbmc/media/movies",
    "--recursive",
    "--fanart",
    "use-existing",
]
code = subprocess.call(cmd)

xbmc.executebuiltin("UpdateLibrary(video)")

xbmcgui.Dialog().ok(addonname, ".nfo files generated!")
