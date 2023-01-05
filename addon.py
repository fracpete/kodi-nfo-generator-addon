import xbmcaddon
import xbmcgui
import subprocess

addon     = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')

# movies
cmd = [
    "kodi-nfo-gen", 
    "--dir",
    "/media/xbmc/media/movies",
    "--recursive",
    "--fanart",
    "download-missing",
]
code = subprocess.call(cmd)

# tv shows
cmd = [
    "kodi-nfo-gen", 
    "--dir",
    "/media/xbmc/media/tvshows",
    "--recursive",
    "--fanart",
    "download-missing",
    "--episodes",
]
code = subprocess.call(cmd)

xbmc.executebuiltin("UpdateLibrary(video)")

xbmcgui.Dialog().ok(addonname, ".nfo files generated!")
