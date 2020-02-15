# kodi-nfo-generator-addon
Addon for kodi to integrate the kodi-nfo-generator tool.

## Notes

* You need to update the path to the movies in the `addon.py` file
  to suit your needs.
* The `kodi-nfo-gen` tool will runs as user `kodi`, therefore you need
  to ensure that this user has write access in the movie directories.
  Otherwise, no `.nfo` files can be generated.
