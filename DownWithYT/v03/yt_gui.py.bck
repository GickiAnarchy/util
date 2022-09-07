#!/usr/bin/env python3
import os
import io
from PIL import Image, ImageTk
import PySimpleGUI as sg
from pytube import YouTube, Search
from v03.yt import YT, TRACK_7


global T7
T7 = YT(TRACK_7)

images = ["images/green_light.png", "images/red_light.png"]


#
#
class YT_GUI():
    global imgs2
    imgs2 = []
    def __init__(self):
        sg.set_options(font = ("Helvetica", 8))

    @staticmethod
    def ask_search():
        sch = []
        ret = []
        lo = [
            [sg.Input("Enter search.....", size = (25, 1), do_not_clear = False, k = "search_input"), sg.Button("Search", k = "search_btn"), sg.Button("Cancel", k = "cancel_btn")],
            [sg.Listbox(ret, size = (30,10), enable_events = True, k = "results_box"), sg.B("Info", k = "info_btn")]
                ]
        win2 = sg.Window("Search", lo, finalize = True)
        while True:
            event, values = win2.read()
            resultsf = win2["results_box"]
            
            if event in (sg.WINDOW_CLOSED, "cancel_btn"):
                break
            if event == "search_btn" and win2["search_input"] is not None:
                search = values["search_input"]
                sch = Search(search)
                re = sch.results
                for r in re:
                    n = YT(r)
                    ret.append(n)
                resultsf.update(ret)
            if event == "info_btn" and len(values["results_box"]):
                YT_GUI().yt_info(values["results_box"][0])
        exit()


    @staticmethod
    def yt_info(yts: YT, imgs2 = imgs2):
        ''' Info Window '''
        image_elem = sg.Image(data = YT_GUI.get_picture(yts.does_exist()), k = "i", metadata = False)
        sg.set_options(font = ("Helvetica", 8))
        lo = [
            [sg.Text("Title:"), sg.Text(yts.title, text_color = "Blue"), image_elem],
            [sg.Text(f"Author:"), sg.Text(yts.author, text_color = "Blue"), sg.Text(f"Length:"), sg.Text(yts.length, text_color = "Blue")],
            [sg.HSeparator()],
            [sg.Text("YouTube ID:", font = ("Helvetica", 6)), sg.Text(yts.id, font = ("Helvetica", 6))],
            [sg.Text("URL", font = ("Helvetica", 6)), sg.Text(yts.url, font = ("Helvetica", 6))],
            [sg.Button("Download", k = "btn_dl", disabled = yts.does_exist(), size = (10,1)), sg.Button("Ok", key = "btn_ok", size = (10,1)), sg.B("useless")]
                ]
        win = sg.Window("Info", lo, finalize = True)
        while True:
            event, values = win.read()
            if event in (sg.WINDOW_CLOSED, "btn_ok"):
                break
            if event == "btn_dl":
                yts.download_audio()
                yts.write_file()
            if event is not None:
                win.refresh()
        win.close()
        return

    @classmethod
    def get_picture(cls, val, imgs2 = imgs2):
        if len(imgs2) == 0:
            for i in images:
                tmp = YT_GUI().get_img_data(i, first = True)
                imgs2.append(tmp)
        if val == True:
            return imgs2[1]
        if val == False:
            return imgs2[0]

    @classmethod
    def get_img_data(cls, f, maxsize=(50, 50), first=False):
        """Generate image data using PIL"""
        img = Image.open(f)
        img.thumbnail(maxsize)
        if first:                     # tkinter is inactive the first time
            bio = io.BytesIO()
            img.save(bio, format="PNG")
            del img
            return bio.getvalue()
        return ImageTk.PhotoImage(img)

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


    @classmethod
    def faask(cls):
        ret = []
        typed = sg.popup_get_text("Search YouTube:")
        search = Search(typed)
        orig = search.results
        for item in orig:
            temp = YT(item)
            ret.append(temp)
        __class__.list_info(ret)


    @staticmethod
    def list_info(results):
        df = sg.DEFAULT_FONT
        fsz = (df[1]/2)
        sg.set_options(font = (df[0],int(fsz)+2))
        selected = None

        btns = [[sg.Button("Download", key = "btn_dl"),sg.Button("Close", key = "btn_close")]]
        info = [[sg.Text("Title:"),sg.Text("..", key = "title")],
        [sg.Text("Channel:"),sg.Text("..", key = "channel"),sg.Text("Length:"),sg.Text("..", key = "length")],
        [sg.Text("", key = "description", size = (30,10), expand_x = True, justification='c')],
        [sg.Text("", key = "tags")]]

        lo = [
        [sg.Combo(results, enable_events = True, key = "results")],
        [sg.Frame('', info, element_justification = "Center", expand_x = True, expand_y = True)],
        [sg.Frame('', btns, element_justification = "Center", expand_x = True)]
        ]
        win = sg.Window("dwYT", lo, element_justification = "c", size = (720,550), finalize = True)
        win.Maximize()
        while True:
            event, values = win.read()
            title = win["title"]
            channel = win["channel"]
            length = win["length"]
            desc = win["description"]
            tags = win["tags"]
            if event in ("btn_close", sg.WINDOW_CLOSED):
                break
            if event == "btn_dl":
                sg.popup("Feature Not Ready Yet")
            if event == "results":
                selected = values["results"]
                try:
                    title.update(selected.title)
                    channel.update(selected.author)
                    length.update(selected.length)
                    desc.update(selected.description)
                    tags.update(selected.tags)
                except Exception as e:
                    sg.popup(e.with_traceback())
                    break
        return


    @staticmethod
    def run():
        YT_GUI.faask()

#
#
if __name__ == "__main__":
    YT_GUI.run()
