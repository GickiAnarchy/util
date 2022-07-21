import os
import PySimpleGUI as sg
import base64images
from PIL import Image

DEFAULT_DIR = os.path.dirname(__file__)


def pop_save():
    pop = sg.popup_get_file("Save File: ", title = "Down with YT", default_extension = ".fa", save_as = True)
    if pop in (None, "Cancel"):
        return False
    return pop

def pop_load():
    pop = sg.popup_get_file("Load File: ", title = "Down with YT", default_extension = ".fa")
    if pop in (None, "Cancel"):
        return False
    return pop

def pop_oops(msg = "There was a problem downloading."):
    pop = sg.popup_error(f"OOPS!! {msg}", auto_close = True, auto_close_duration = 5)
    return pop

def splash():
    layout = [[sg.Image(data = base64images.DWY_LOGO)]]
    win = sg.Window("Down With YT", layout, finalize = True, modal = True, alpha_channel = 1, no_titlebar=True, keep_on_top=True, auto_close = True, auto_close_duration = 5)
    return win


layout_tagger = [[sg.FileBrowse()]]

def open_tagger():
    tagger = sg.Window("CArL", layout_tagger, finalize = True, modal = True, alpha_channel = 1, no_titlebar=True)
    while True:
        event, values = tagger.read()
        if event == sg.WIN_CLOSED:
            tagger.close()

def loginWindow():
    passed = False
    layout = [[sg.Text("Name: "), sg.Input("", key = "NAME")],
                    [sg.Text("Password: "), sg.Input("", key = "PASSWORD")],
                    [sg.Button("Submit", key = "SUBMIT_BTN"), sg.Button("Cancel", key = "CANCEL_BTN")]]
    window = sg.Window("Login", layout, finalize = True)
    
    while True:
        event, values = window.read()
        name = window["NAME"]
        pw = window["PASSWORD"]
        
        if event in ("CANCEL_BTN", sg.WINDOW_CLOSED):
            break
        
        if event == "SUBMIT_BTN":
            if name == pw:
                passed = True
            name.update("")
            pw.update("")
            sg.popup_auto_close(f"Incorrect {name} {pw}")
            break

    window.close()
    return passed