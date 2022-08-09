''' GUI For v.0.2 '''
import PySimpleGUI as sg
from b64_images import *


class DWYT_GUI:
    def __init__(self):
        self.main_window = None


    def makeLayouts(self):
        self.main_buttons = [sg.Button("Save", k = "btn_save"), sg.Button("Load", k = "btn_load"), sg.Button("Quit", k = "btn_quit")]


if __name__ == "__main__":
    pass