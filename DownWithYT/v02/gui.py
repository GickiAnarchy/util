''' GUI For v.0.2 '''
import PySimpleGUI as sg
from dwyt2 import DWYT


class DWYT_GUI:
    def __init__(self):
        self.dwyt = DWYT()

    def makeLayouts(self):
        d_font = sg.DEFAULT_FONT
        
        main_buttons = [[sg.Frame("tabs", [[sg.Button("Save", k = "save_btn"), sg.Button("Load", k = "load_btn"), sg.Button("Quit", k = "quit_btn")]])]]
        
        search_layout = [[sg.Input("", k = "search_input"), sg.Button("Search", k = "search_btn")],
                                    [sg.Listbox(self.dwyt.results, k = "results_list", size = (45, 15))]]

        home_layout = []

        saved_layout = []

        about_layout = []


        layout = [[sg.Text("Down With YouTube")]]
        layout += [[sg.TabGroup(
                            [[sg.Tab("Home", home_layout),
                            sg.Tab("Search", search_layout),
                            sg.Tab("Saved List", saved_layout),
                            sg.Tab("About", about_layout)]],
                        key = "tabs", expand_x = True, expand_y = False),
                        ]]
        layout += [[sg.Frame("123456", main_buttons)]]
        layout[-1].append(sg.Sizegrip())
        return layout


    def makeWindow(self):
        l = self.makeLayouts()
        main_window = sg.Window("Down With YouTube", l, size = (768, 500), grab_anywhere = True , finalize = True)
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