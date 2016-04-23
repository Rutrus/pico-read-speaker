## Pico-read-speaker :: text2wav :: pico2wave

Native package `pico2wave` takes into account a limited number of characters, this script solves this problem.
`text2wav.py` converts completely from the clipboard or a file to spoken words. 
The limit of characters are in theory, unlimited.


Authors : Various (@mickaelh @rutrus)

Version : 1.1.0

Licence : GPL v3

## Required

System: It compiles under linux kernels: Debian, Ubuntu, Maemo ...

The SVOX Pico engine is a software speech synthesizer for German, English (GB and US), Spanish, French and Italian.

Installation required :
    - libttspico* (`pico2wave` command)
    - gtk2 module for python

If you have Ubuntu or Debian-based distro:
    sudo apt-get install libttspico-utils python-gtk2-dev

## How to use this script
    $ ./text2wav.py [-i <input text file>] [-l|--lang fr-FR]

If you select your text and copy it (ctrl+c), then execute `./text2wav.py` command terminal
If you have a txt file instead execute `./text2wav.py -i 'yourtextfile.txt'`

**Note:**
The optional parameter [-l | --lang] is by default = en-US
You can edit default language in line 53. e.g. `default_lang = 'es-ES'`

In the current directory of "text2wav.py" it will generate only one file named `chapter.wav`

If you have ffmpeg installed you can uncomment line 155, then the file will convert it to `chapter.mp3`

Good listening.
