## Pico-read-speaker :: text2wav :: pico2wave

Native package `pico2wave` takes into account a limited number of characters, this script solves this problem.
`text2wav.py` converts completely from the clipboard or a file to spoken words. 
The limit of characters are in theory, unlimited.


Authors : Various (@mickaelh @rutrus)

Version : 1.2.0

Licence : GPL v3

## Required

System: It compiles under linux kernels: Debian, Ubuntu, Maemo ...

The SVOX Pico engine is a software speech synthesizer for German, English (GB and US), Spanish, French and Italian.

Installation required:
- libttspico* (`pico2wave` command)
- gtk2 module for python

If you have Ubuntu or Debian-based distro: `sudo apt-get install libttspico-utils python-gtk2-dev`
    
If you want convert wav into mp3 then:
- Install ffmpeg or libav-tools: `sudo apt-get install ffmpeg`
- Turn line 50 to `True`
    
## How to use this script
    $ ./text2wav.py [-i <input text file>] [-l|--lang fr-FR] [-o <sound-file.mp3>]
    
- If you select and copy your text (ctrl+c), then execute `./text2wav.py` in a command terminal
- You can also choose a name for the output file `./text2wav.py -o "Your sound file.mp3"` by default it outputs *chapter.[wav|mp3]*
- If your source is in txt file instead execute `./text2wav.py -i 'yourtextfile.txt'`

**Note: You can config some things**
- Line 46: The optional parameter [-l | --lang] is by default `--lang 'en-US'`. You can config default_lang in line 46.
- Line 48: In the current directory of "text2wav.py" it will generate by default only one file named `chapter.wav` or `chapter.mp3`
- Line 50: You can turn on the mp3 converter switching it to `True` after installing ffmpeg.

Good listening.
