# kodi-nfo-generator-addon
Addon for kodi to integrate the kodi-nfo-generator tool.

## Requirements

[kodi-nfo-generator](https://github.com/fracpete/kodi-nfo-generator) must be installed on the system:

```
sudo pip install kodi-nfo-generator
```

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
  Or, if you are running kodi as the `pi` user:
  ```
  /home/pi/.kodi/addons/kodi-nfo-generator-addon/addon.py
  ```


## Notes

* You need to update the path to the movies in the `addon.py` file
  to suit your needs.
* The `kodi-nfo-gen` tool will run as user `kodi`, therefore you need
  to ensure that this user has write access in the movie directories.
  Otherwise, no `.nfo` files can be generated. 


## Custom TV show episode naming conventions

If your naming conventions for TV show episodes does not follow the `S??E??*.*` pattern, then you can use the `--episode_pattern`, `` and `` options to adjust the matching and extraction. 

If you use `?x??*.*` (e.g., 1x07.mkv) as your convention, you can append the following parameters to correctly match the files and extract the season/episode information to generate `.nfo` files:

```
    "--episode_pattern",
    "?x??*",
    "--season_group",
    "([0-9]?[0-9])x[0-9][0-9].*",
    "--episode_group",
    "[0-9]?[0-9]x([0-9][0-9]).*",
```


## Links

* Hello World - https://kodi.wiki/view/HOW-TO:HelloWorld_addon
* API - https://kodi.wiki/view/List_of_built-in_functions#Library_built-in.27s

