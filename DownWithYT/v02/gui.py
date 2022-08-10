''' GUI For v.0.2 '''
import PySimpleGUI as sg
from b64_images import *


class DWYT_GUI:
    def __init__(self):
        self.main_window = None


    def makeLayouts(self):
        main_buttons = [sg.Button("Save", k = "btn_save"), sg.Button("Load", k = "btn_load"), sg.Button("Quit", k = "btn_quit")]
        
        search_layout = None

        home_layout = None

        saved_layout = None

        about_layout = None


        layout = [[]]
        layout += [[sg.TabGroup(
                            [[sg.Tab("Home", home_layout),
                            sg.Tab("Search", search_layout),
                            sg.Tab("Saved List", saved_layout),
                            sg.Tab("About", about_layout)]],
                        key = "tabs", expand_x = True, expand_y = True),
                        ]]

        layout[-1].append(sg.Sizegrip())

if __name__ == "__main__":
    pass