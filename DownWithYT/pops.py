import os
import PySimpleGUI as sg
import base64images
import json
from PIL import Image

DEFAULT_DIR = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".", ".data"))
users_file = f"{data_dir}/.users.json"

if not os.path.isfile(users_file):
    tmpusers = {"NAME" : "PASSWORD"}
    with open(users_file, "w") as usersfile:
        json.dump(tmpusers, usersfile)

#
##
###
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

#
##
###
def read_users():
    with open(users_file, "r") as u_file:
        users = json.load(u_file)
        u_file.close()
    return users

def write_users(users, clear = False):
    if clear == True:
        users = {"NAME" : "PASSWORD"}
    with open(users_file, "w") as f:
        json.dump(users, f)
        f.close()

def get_users_string():
    u = read_users()
    data = json.dumps(u, indent = 2)
    return data

def create_user():
    layout_right = [[sg.Input("", key = "NAME")], [sg.Input(password_char = "*", key = "PASSWORD")], [sg.Input(password_char = "*", key = "PASSWORD2")]]
    layout_left = [[sg.Text("Name: ")], [sg.Text("Password: ")], [sg.Text("Re-enter Password")]]
    layout = [[sg.Frame("", layout_left, element_justification = "Right", border_width= 0), sg.Frame("", layout_right, border_width= 0)], [sg.Button("Submit", key = "SUBMIT_BTN"), sg.Button("Cancel", key = "CANCEL_BTN")]]
    window = sg.Window("Create a user", layout,  modal = True, keep_on_top = True, finalize = True)
    users = read_users()
    while True:
        event, values = window.read()
        name = values["NAME"]
        pw = values["PASSWORD"]
        pw2 = values["PASSWORD2"]
        if event in ("CANCEL_BTN", sg.WINDOW_CLOSED):
            break
        if event == "SUBMIT_BTN":
            if name in users.keys():
                sg.popup_auto_close("Username taken")
            elif not name in (None, "") and pw == pw2:
                users[name] = f"{pw}"
                write_users(users)
                sg.popup_auto_close(f"{name} added to users")
                break
    window.close()

##
def login_window():
    layout_right = [[sg.Input("", key = "NAME")], [sg.Input(password_char = "*", key = "PASSWORD")]]
    layout_left = [[sg.Text("Name: ")],[sg.Text("Password: ")]]
    layout = [[sg.Frame("", layout_left, element_justification = "Right"), sg.Frame("", layout_right)],
                  [sg.Button("Submit", key = "SUBMIT_BTN"), sg.Button("Cancel", key = "CANCEL_BTN")]]
    window = sg.Window("Login", layout, modal = True, finalize = True, keep_on_top = True)
    users = read_users()
    passed = False
    while True:
        event, values = window.read()
        name = values["NAME"]
        pw = values["PASSWORD"]
        if event in ("CANCEL_BTN", sg.WINDOW_CLOSED):
            break
        if event == "SUBMIT_BTN":
            if name in users.keys():
                if users.get(name) == pw:
                    passed = True
                else:
                    sg.popup_auto_close("Incorrect")
            else:
                sg.popup_auto_close(f"{name} is not an authorized user")
            window["NAME"].update("")
            window["PASSWORD"].update("")
            break
    window.close()
    return passed