''' GUI For v.0.2 '''
import PySimpleGUI as sg
from dwyt2 import DWYT


class DWYT_GUI:
    def __init__(self):
        self.dwyt = DWYT()

    def makeLayouts(self):
        d_font = ("Helvetica", 8)
        sg.set_options(font = d_font, button_element_size = (2, 1), scaling = 1.8)
        
        main_buttons = [[sg.Frame(" ", [[sg.Button("Save", k = "save_btn"), sg.Button("Load", k = "load_btn"), sg.Button("Quit", k = "quit_btn")]], element_justification = "Center")]]

        search_layout = [[sg.Input("", k = "search_input"), sg.Button("Search", k = "search_btn")],
                                    [sg.Listbox(self.dwyt.results, k = "results_list", size = (45, 15), expand_y = True)]]

        home_layout = []

        saved_layout = []

        about_layout = []


        layout = [[sg.Text("Down With YouTube")]]
        layout += [[sg.TabGroup(
                            [[sg.Tab("Home", home_layout),
                            sg.Tab("Search", search_layout),
                            sg.Tab("Saved List", saved_layout),
                            sg.Tab("About", about_layout)]],
                        key = "tabs", expand_x = True, expand_y = True),
                        ]]


        layout[-1].append(main_buttons)
        layout[-1].append(sg.Sizegrip())
        return layout


    def makeWindow(self):
        l = self.makeLayouts()
        main_window = sg.Window("Down With YouTube", l, size = (768, 500), grab_anywhere = True, element_justification = "Center", finalize = True)
        return main_window


    def runn(self):
        win = self.makeWindow()
        while True:
            event, values = win.read()
            if event in ("quit_btn", sg.WIN_CLOSED):
                break

            if event == "search_btn":
                if values["search_input"] not in ("", None):
                    self.dwyt.searchYT(values["search_input"])
                    win["results_list"].update(self.dwyt.results)

            if event is not None:
                pass


if __name__ == "__main__":
    p = DWYT_GUI()
    p.runn()