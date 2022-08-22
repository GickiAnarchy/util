import PySimpleGUI as sg
from v03.yt import YT, TRACK_7

global T7
T7 = YT(TRACK_7)

class YT_GUI():
    def __init__(self):
        sg.set_options(font = ("Helvetica", 8))
    
    @staticmethod
    def yt_info(yt: YT):
        ''' Info Window '''
        sg.set_options(font = ("Helvetica", 8))
        lo = [
            [sg.Text("Title:"), sg.Text(yt.title, text_color = "Blue")],
            [sg.Text(f"Author:"), sg.Text(yt.author, text_color = "Blue"), sg.Text(f"Length:"), sg.Text(yt.length, text_color = "Blue")],
            [sg.HSeparator()],
            [sg.Text("YouTube ID:", font = ("Helvetica", 6)), sg.Text(yt.id, font = ("Helvetica", 6))],
            [sg.Text("URL", font = ("Helvetica", 6)), sg.Text(yt.url, font = ("Helvetica", 6))],
            [sg.Button("Download", k = "btn_dl", disabled = yt.does_exist(), size = (10,1)), sg.Button("Ok", key = "btn_ok", size = (10,1))]
                ]
        win = sg.Window("Info", lo, finalize = True)
        while True:
            event, values = win.read()
            if event in (sg.WINDOW_CLOSED, "btn_ok"):
                break
            if event is not None:
                win.refresh()
        win.close()
        return

    @staticmethod
    def yt_related(y: YT):
        lo = [
            [sg.Text(), sg.Text(f"Search for \"{y.title}\""), sg.Text()],
            [sg.Listbox(y.related_titles(), size = (50, 20), font = ("Helvetica", 6), k = "related")],
            [sg.Button("Ok", k = "btn_ok"), sg.Button("Get", k = "btn_get")]
                ]
        win = sg.Window("Related Videos", lo, finalize = True)
        while True:
            event, values = win.read()
            if event in (sg.WINDOW_CLOSED, "btn_ok"):
                break
            if event == "btn_get":
                if len(values["related"]) != 0:
                     y2 = YT(values["related"])
                     YT_GUI.yt_info(y2)
        win.close()
        return
        



    @staticmethod
    def run():
        YT_GUI.yt_info(T7)
        YT_GUI.yt_related(T7)


if __name__ == "__main__":
    YT_GUI.run()