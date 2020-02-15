import xbmcaddon
import xbmcgui
import subprocess

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

subprocess.call([
    "kodi-nfo-gen", 
    "--dir",
    "/media/xbmc/media/movies",
    "--recursive",
    "--fanart",
    "use-existing",
])

xbmcgui.Dialog().ok(addonname, ".nfo files generated!")
