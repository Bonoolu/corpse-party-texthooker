# Corpse Party Texthooker
Text and audio hooker for the visual novel Corpse Party (2021) with Anki integration
## 
## Prerequisites

A working anki mining setup with yomichan. [Here is a tutorial](https://www.youtube.com/watch?v=OJxndUGN8Cg)

## Dependencies

[dnspy](https://github.com/dnSpy/dnSpy) is needed for patching the game and installing the texthooker.

[AssetStudio](https://github.com/Perfare/AssetStudio) is needed for extracting all the audio files from the visual novel

[ffmpeg](https://ffmpeg.org/) is needed to convert all the audio files from .wav to .opus This reduces the filesize from 6.9G down to 366M

[imagemagick](https://imagemagick.org/) is needed to reduce the image size of the screenshot

## Dependencies if you are on Linux or BSD
- xdotool and maim are needed to take a screenshot of the visual novel

## Notice about macOS
The only script in this repo which wont work on macOS is [corpse-screenshot.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/corpse-screenshot.sh)
If you'll have to replace this script with something lese if you want screenshots in you anki notes.

## Notice about Windows
The texthooker should work out of the box, but the audio hooker and screengrabber wont.
Two scripts in this repo wont work on windows [corpse-screenshot.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/corpse-screenshot.sh) and
[usr1anki.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/usr1anki.sh)
You could probably do something similar with shareX or with AutoHotKey.

## Explanation for each file in this repo

- [inject.cs](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/inject.cs)

  This is the texthooker. The file itself contains a tutorial on how to use it. This file puts audio filenames and dialog lines into the clipboard like this:
  \[Sound:AYU_0000\] ありがとう. You install this code with dnspy. 
  If you are on linux or macOS then you have to execute dnspy with [wine](https://www.winehq.org/)

- [anki-addon](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/anki-addon)

  This addon contains the code to update the most recent anki note with audio and a screenshot of the game.
  This addon monitors the clipboard and removes the audio filename from the clipboard after memorizing it.
 
- [corpse-screenshot.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/corpse-screenshot.sh)

  A script which creates a new screenshot of the visual novel and saves it in /tmp/. This script only works on linux.
  
- [usr1anki.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/usr1anki.sh)

  This script sends a signal to the anki addon to update the most recent note. You need to bind the script to a shortcut in your operating system.
  This script works on Linux/BSD/macOs, but not on windows.
  
- [convert.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/convert.sh)

  A script which converts all the audio files from wav to opus.
## Summary how everything works

1. The user opens Anki and starts the Addon by clicking Tools -> Start corpse party addon

2. The user opens the visual novel and loads a chapter

3. The modded viusal novel itself puts a new audio filename and text line into the clipboard:

    Example Clipboard: \[Sound:AYU_0000\] ありがとう.
4. The anki addon saves the audio filename and removes the filename from the clipboard:

    Example Clipboard: ありがとう.
5. The user sees the Sentence in Yomichan and adds one word to anki

6. The user presses a shortcut to execute usr1anki.sh which sends an USR1 unix signal to the anki addon

7. The anki addon adds the audio file from step 4 to the most recent anki note

8. The anki addon executes corpse-screenshot.sh and adds the pictures to the most recent anki note

## How to install
If you are using macOS or Windows then please read notice about your Operating System.
Step 1 should work on ANY operating system.
Step 1 is only the text hooker without the audio hooker or the screen grabber.

1. Patch the visual novel with dnspy to install the texthooker, please look at the contents of [inject.cs](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/inject.cs)
, if you aren't on windows then you have to execute it with wine

2. Extract all audio files with [AssetStudio](https://github.com/Perfare/AssetStudio), if you aren't on windows then you have to execute it with wine

3. Convert all the audio files with ffmpeg to opus. Linux users can use [convert.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/convert.sh). Windows users can use [QWinFF](https://qwinff.github.io/)

4. If you don't have a 4k Display, edit this file and change the numbers to match your screen size [corpse-screenshot.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/corpse-screenshot.sh) 

5. Edit the anki mod [anki-mod/__init__.py](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/anki-mod/__init__.py)

    4.1. change the path to your audio files on line 65

    4.2. change the path to corpse-screenshot.sh on line 55 OR just put the file into your PATH

6. Install the anki-addon by moving the anki-addon directory to .local/share/Anki2/addons21 or C:\Users\Administrator\AppData\Roaming\Anki2\addons21

7. Create a keyboard shortcut in your operating system to [usr1anki.sh](https://github.com/Bonoolu/corpse-party-texthooker/blob/main/usr1anki.sh)

## How to Use

1. Open up Anki and Corpse Party (2021), then start the visual novel by loading a chapter

2. At this point, dialog should appear in yomichan, mine a word and add it to anki

3. Press the shortcut you created to update the last anki note with audio and picture
