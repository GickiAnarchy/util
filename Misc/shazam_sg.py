import os
import PySimpleGUI as sg
from v03.yt import YT
from ShazamAPI import Shazam


song = sg.popup_get_file("Choose a song")

if song == None:
    exit()

pth, s = os.path.split(song)
name, ext = os.path.splitext(s)
info = f"{pth}\n{s}\n{name}\n{ext}"
sg.popup_ok(info)    #checking the splitting

if ext.lower() not in (".mp3", ".wav"):
    exit()

mp3_file_content_to_recognize = open(song, 'rb').read()

shazam = Shazam(mp3_file_content_to_recognize)
recognize_generator = shazam.recognizeSong()
while True:
	sg.popup_ok(next(recognize_generator))
