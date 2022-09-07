#!/usr/bin/env python3
import os, io, sys
from PIL import Image, ImageTk
import PySimpleGUI as sg
from pytube import YouTube, Search
from v03.yt import YT, TRACK_7

# debug variables #
T7 = YT(TRACK_7)

# images #
light_images = ["images/green_light.png", "images/red_light.png"]

# sg.<settings> #
sg.MENU_SHORTCUT_CHARACTER = '&'
sg.theme('dark green 7')
sg.theme('dark amber')

# menubar #
menu_def = [["&Menu",["Search"]],
            ["E&xit",["Exit"]]]
menu_bar = [sg.Menu(menu_def, tearoff=False, key='-MENU-')]

# layouts #
search_top = [sg.Text("Search YouTube: "), sg.Input("", key = "search_input"),sg.Button("Search", key = "btn_search")],[sg.Listbox([""], size = (30,5), key = "search_results")]

search_bottom = [sg.Button("Add", key = "btn_add"),sg.Text(""), sg.Button("Remove", key =   "btn_remove")],[sg.Text(""), sg.Button("Clear", key = "btn_clear"), sg.Text("")]

search_layout = [[sg.Frame("", search_top, element_justification = "Center", relief = sg.RELIEF_FLAT)],[sg.Frame("", search_bottom, element_justification = "Center", relief = sg.RELIEF_FLAT, expand_x = True)]]

layout = [menu_bar,search_layout]

# windows #
win = sg.Window("dwYT", layout, element_justification = "Center", size = (900,400), finalize = True)


# run #
def run():
    event, values = win.read()

    while True:


        if event in ("Exit", sg.WINDOW_CLOSED):
            break


        #search layout
        if event == "btn_clear":
            sg.popup_ok("Results Cleared")
            print("cleared results")

        if event == "btn_search":
            print("search button")

        if event is not None:
            print("not None")

    sys.exit()




if __name__ == "__main__":
    run()