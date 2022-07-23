import os
import PySimpleGUI as sg
import base64images
import json
from PIL import Image

DEFAULT_DIR = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".", ".data"))
users_file = f"{data_dir}/.users.json"
config = f"{data_dir}/.config.fa"

if not os.path.exists(config):
    with open(config, "x") as f:
        f.close()

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

#
##
def lock_window():
    lock = False
    top = [sg.Text("Enter a lock password")]
    left = [[sg.Text("Password:")], [sg.Text("Verify Password: ")]]
    right = [[sg.Input(password_char = "*", key = "pw1")], [sg.Input(password_char = "*", key = "pw2")]]
    bottom = [sg.Button("Ok", key = "OK"), sg.Button("Cancel", key = "CANCEL")]
    layout = [top, [sg.Frame(None, left, p = 0), sg.Frame(None, right, p = 0)], bottom]
    window = sg.Window("Lock DwYT", layout, modal = True, keep_on_top = True, finalize = True)
    while True:
        event, values = window.read()
        pw1 = values["pw1"]
        pw2 = values["pw2"]
        if event in (sg.WINDOW_CLOSED, "CANCEL"):
            lock = False
            break
        if event == "OK":
            if pw1 == pw2:
                with open(config, "w") as c:
                    c.write("True" + "\n")
                    c.write(pw1)
                lock = True
                break
            window["pw1"].update(background_color = "Red")
            window["pw2"].update(background_color = "Red")
    window.close()
    return lock

def unlock_window():
    lock = True
    layout = [[sg.Text("|—Enter Lock Code—|")],
                     [sg.Input(key = "pw", password_char = "*")],
                     [sg.Button("Unlock", key = "UNLOCK"), sg.Button("Cancel", key = "CANCEL")]]
    window = sg.Window("Unlock", layout, modal = True, keep_on_top = True, finalize = True)
    state, code = get_config()
    while True:
        event, values = window.read()
        pw = values["pw"]
        if event in (sg.WINDOW_CLOSED, "CANCEL"):
            break
        if event == "UNLOCK":
            if pw == code:
                lock = False
            break
    window.close()
    return lock

def get_config():
    with open(config, "r") as c:
        is_locked = bool(c.readline())
        code = c.readline()
        c.close()
    return (is_locked, code)