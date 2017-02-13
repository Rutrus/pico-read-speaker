#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Transform text in wav audio
#exec : text2wav.py

u"""
Authors : Mickaelh, Rutrus
version : 1.2.1
Licence : GPL v3

Description: Native package `pico2wave` takes into account a limited number of
characters, this script solves this problem. `text2wav.py` converts completely
from the clipboard or a file to spoken words.
The limit of characters are in theory, unlimited.

## Required
System: It compiles under linux kernels: Debian, Ubuntu, Maemo ...
The SVOX Pico engine is a software speech synthesizer for German, English (GB and US), Spanish, French and Italian.

Installation required:
    - libttspico* (`pico2wave` command)
    - gtk2 module for python
Optional:
    - ffmpeg

## How to use this script
    $ ./text2wav.py [-i <input text file>] [-l|--lang fr-FR] [-o <sound-file.mp3>]

- If you select and copy your text (ctrl+c), then execute `./text2wav.py` in a command terminal
- You can also choose a name for the output file `./text2wav.py -o "Your sound file.mp3"` by default it outputs *chapter.[wav|mp3]*
- If your source is in txt file instead execute `./text2wav.py -i 'yourtextfile.txt'`

**Note: You can config some things**
- Line 48: The optional parameter [-l | --lang] is by default `--lang 'en-US'`. You can config default_lang in line 46.
- Line 50: In the current directory of "text2wav.py" it will generate by default only one file named `chapter.wav` or `chapter.mp3`
- Line 52: You can turn on/off the mp3 converter. If ffmpeg is installed it will switch to True.

Good listening.

TODO:
    Development of the text file part and manage multiple text file so ilimiter vocalize books completely.
"""
from __future__ import print_function
import os, sys, gtk, getopt, wave

# START CONFIG
#Choose default language between: 'en-US','en-GB','de-DE','es-ES','fr-FR','it-IT'
default_lang = 'en-US'
#Default name of .wav or .mp3 file
default_outfile = 'chapter'
#Convert to mp3? Install ffmpeg before
is_ffmpeg_installed = (os.system('which ffmpeg') == 0)
# END CONFIG

limit_char=30000
# get text from (ctrl + c)
def text_clipboard():
    clipboard = gtk.clipboard_get()
    return clipboard.wait_for_text()

#get text from file
def text_file(arg):
    try:
        f = open(arg, 'r')
    except IOError:
        print("Error: file not found", file=sys.stderr)
        return 1
    return f.read()

#cut the text by sentence
def casier_txt(list_txt):
    current_letter=0
    list_sentence = []
    list_chapter = []

    for sentence in list_txt:
        current_letter = current_letter + len(sentence) + 2 # It will add dot and space chars too
        if limit_char < current_letter:
            if list_sentence:
                list_chapter.append(list_sentence)
                list_sentence = []
                list_sentence.append(u'%s.' % sentence)
                current_letter = len(sentence) + 2
            else:
                # First sentence longer than 3000 characters
                print("Sentence may be truncated (>3000 characters):\n%s..." % sentence[:200] , file=sys.stderr )
                list_sentence.append(u'%s.' % sentence)
                list_chapter.append(list_sentence)
                list_sentence = []
                current_letter = 0
        else:
            list_sentence.append(u'%s.' % sentence)

    if list_sentence:
        list_chapter.append(list_sentence)

    return list_chapter

def joinwavs(outfile):
    infiles = []

    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.startswith('article_picotts_') and f.endswith('.wav'):
                infiles.append(f)

    if len(infiles) > 1:
        print("Joining wav files into %s" %outfile, file=sys.stderr)
        data = []
        for infile in infiles:
            w = wave.open(infile, 'rb')
            data.append( [w.getparams(), w.readframes(w.getnframes())] )
            w.close()

        output = wave.open(outfile, 'wb')
        output.setparams(data[0][0])
        for params,frames in data:
            output.writeframes(frames)
        output.close()
        for f in infiles:
            os.remove(f)
    else:
        os.rename(infiles[0], outfile)
    return outfile

def wav2mp3(infile):
    outfile = '%s.mp3' % infile[:-4]
    print("'%s' will be replaced with '%s'" %(infile,outfile), file=sys.stderr)
    try:
        os.remove(outfile)
    except: pass
    os.system('ffmpeg -i "%s" -codec:a libmp3lame "%s"' % (infile, outfile))
    os.remove(infile)
    return outfile

# execute command line pico2wave
def text_to_speech(txt,lang):
    list_lang = ['en-US','en-GB','de-DE','es-ES','fr-FR','it-IT']
    if lang not in list_lang:
        lang = default_lang

    txt = txt.replace('"','')
    txt = txt.replace('[','(')
    txt = txt.replace(']',')')
    txt = txt.replace('.\n','. ')
    #txt = txt.replace('\n\n','. ')
    total_letter = len(txt)
    if total_letter > 1:
        list_txt = txt.split('. ')
        list_txt = filter(None, list_txt)
    else:
        list_txt = []

    if list_txt:
        position = casier_txt(list_txt)

    else:
        print("No sentences founded", file=sys.stderr)
        return 1

    delete = []
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            if f.startswith('article_picotts_') and f.endswith('.wav'):
                delete.append(f)
    for f in delete:
        os.remove(f)

    for index,value in enumerate(position):
        if value:
            value =' '.join(value)
            print("Translating into %s ..." % (lang))
            os.system('pico2wave -l %s -w article_picotts_%02d.wav "%s"' % (lang, index+1, value))
            print("File Creation: article_picotts_%02d.wav" % (index+1))

    print("Created %d wav files correctly" % (index + 1), file=sys.stderr)

def main(argv):
    lang = ''
    outfile = default_outfile
    if (os.system('which pico2wave') != 0):
        print("You must install pico2wave:")
        print("sudo apt install -y libttspico-utils")
        sys.exit(1)
    try:
        opts, args = getopt.getopt(argv,"hi:l:o:",["help","input_text_file=","lang=","output_wav_file="])
    except getopt.GetoptError:
        sys.exit(2)

    if opts:
        for opt, arg in opts:
            if opt in ('-l','--lang'):
                lang = arg
            else:
                lang = default_lang

            if opt in ('-o', '--output_wav_file'):
                outfile = arg

            if opt in ('-h','--help'):
                print(
'''Usage:
   %s [-i <input_txt>] [-l <lang>] [-o <sound_file.wav>]

Without -i option it verifies if there is a text copied to clipboard

Options:
    -i, --input_text_file   Reads a text file
    -l, --lang              Language. Default: "%s"
    -o, --sound_file   Name of the result file.
                            Default output file: "%s"

Options lang:
    en-US   English
    en-GB   Great Britain
    de-DE   German
    es-ES   Spanish
    fr-FR   French
    it-IT   Italian

Help option:
    -h,--help   show this message'''
                % (sys.argv[0], default_lang, outfile+'.wav' ))
                sys.exit()
            elif opt in ('-i', '--input_text_file'):
                txt = text_file(arg)
            else:
                txt = text_clipboard()
    else:
        txt = text_clipboard()

    text_to_speech(txt,lang)

    if outfile.endswith('.wav') or outfile.endswith('.mp3'):
        outfile = outfile[:-4]
    outfile = joinwavs(outfile+'.wav')

    #If you have ffmpeg installed:
    if is_ffmpeg_installed:
        outfile = wav2mp3(outfile)
    print("Speech complete! The result is in:", file=sys.stderr)
    print("%s" % outfile)
    return 0

if __name__ == "__main__":
   main(sys.argv[1:])
