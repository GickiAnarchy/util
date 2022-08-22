import PySimpleGUI as sg
from v03.yt import YT
from v03.yt import TRACK_7

global T7
T7 = YT(TRACK_7)

class YT_TEST():
    ''' Class to test different gui for YT '''

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
            [sg.Button("Download", k = "btn_dl", disabled = yt.does_exist(".."), size = (10,1)), sg.Button("Ok", key = "btn_ok", size = (10,1))]
                ]
        win = sg.Window("Info", lo, finalize = True)
        while True:
            event, values = win.read()
            win["btn_dl"].update(disabled = yt.does_exist(".."))
            if event in (sg.WINDOW_CLOSED, "btn_ok"):
                break
            if event is not None:
                win.refresh()
        win.close()



if __name__ == "__main__":
    ''' test for info window '''
    YT_TEST.yt_info(T7)