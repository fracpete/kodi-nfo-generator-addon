# kodi-nfo-generator-addon
Addon for kodi to integrate the kodi-nfo-generator tool.

## Installation

* Download the code as a zip file (*Clone or download*)
* Copy the zip file onto your kodi box
* Ensure that you can install addons from zip files
  (Settings / System / Add-ons: enable *Unknown sources*)
* From the main menu, select *Addons* and then *Search*, cancel the search
* Now select *Install from zip file* and select the previously downloaded zip file
* ssh into your kodi box and fix the default path in the Python script to work
  for your setup in the following file:
  ```
  /var/lib/kodi/.kodi/addons/kodi-nfo-generator-addon/addon.py
  ```


## Notes

* You need to update the path to the movies in the `addon.py` file
  to suit your needs.
* The `kodi-nfo-gen` tool will run as user `kodi`, therefore you need
  to ensure that this user has write access in the movie directories.
  Otherwise, no `.nfo` files can be generated. 

