Pico_read_speaker
=================

Using Pico2wave to ease from the recovery text to the clipboard or a file so unlimited.

Pico2wave takes into account a limited number of characters, this program solves this problem.

Author : Mickaelh
version : 1.1.0
Licence : GPL v3

Required
========

System : the compliant systems under linux kernels: Debian, Ubuntu, Maemo ...

The SVOX Pico engine is a software speech synthesizer for German, English (GB
 and US), Spanish, French and Italian.

Installation required :

    - svox (pico2wave) https://packages.debian.org/source/squeeze/svox
    - Python install gtk: $ sudo apt-get install python-gtk2-dev

If you have Ubuntu or Debian-based distro:
    - sudo apt-get install libttspico-utils python-gtk2-dev 

Svox package maemo dispnible on https://openrepos.net/

installation order:

    - libttspico-data (https://openrepos.net/content/mickaelh/libttspico-data)
    - libttspico0 (https://openrepos.net/content/mickaelh/libttspico0)
    - libttspico-utils (https://openrepos.net/content/mickaelh/libttspico-utils)
    - libttspico-dev (https://openrepos.net/content/mickaelh/libttspico-dev)

How to use this script
======================

Select your text and copy it (ctrl+c), then execute a command terminal

    $ ./text2wav.py [-l|--lang fr-FR]
    or
    $ ./text2wav.py -i <input text file> [-l|--lang fr-FR]

Note:
The optional parameter [-l | --lang] by default = en-US
You can edit default language in line 53. e.g. `default_lang = 'es-ES'`

In the current directory of "text2wav.py" it will generate only one file named `chapter.wav`

If you have ffmpeg installed you can uncomment line 155, then the file will convert it to `chapter.mp3`

Good listening.
