#!/bin/bash
maim -i $(ps -aux | grep CorpseParty.x64 | grep -v grep | grep -v SteamLaunch | awk ' { print $2 }' | xargs xdotool search --pid |head -n1) /tmp/corpse-screenshot_full.png
filename=corpse_$(date +%s)
convert /tmp/corpse-screenshot_full.png -crop 3277x1368+345+630 -resize x400 /tmp/"$filename".jpg
echo "/tmp/$filename.jpg"
