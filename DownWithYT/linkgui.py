#pylint:disable=W0702
#pylint:disable=W0612
#pylint:disable=E0401
import os
import random
import pickle
from linklist import LinkList
import PySimpleGUI as sg
from pytube import YouTube, Playlist
from re import search
import base64images
import pops


MAGICK = "https://youtube.com/playlist?list=PLXS7fy2pHgKch6L4xtvybDqxo4tVWAoKK"

GREEN = "#6CD700"
RED = "#D70010"
BLUE = "#0800D7"

data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),".", ".data"))
COMPLETED = f"{data_dir}/all_completed.txt"
BKP = f"{data_dir}/.links.fa.bak"


class LinkGui:
    def __init__(self, linklist = None):
        # Using sg.Print when print() is used to show the terminal output in thr GUI
        print = sg.Print
        #Directory Creation
        if not os.path.isdir(data_dir): os.makedirs(data_dir)
        if not os.path.isdir(f"{data_dir}/Videos"): os.makedirs(f"{data_dir}/Videos")
        if not os.path.isdir(f"{data_dir}/Audio"): os.makedirs(f"{data_dir}/Audio")
        #LinkList Handling
        if linklist == None:
            self.LL = LinkList()
        else:
            self.LL = linklist
        #Save file name, if loaded or saved in session. (To avoid a popup constantly)
        self.saveFile = None

    @property
    def LL(self):
        return self._LL
    @LL.setter
    def LL(self, new_LL):
        self._LL = new_LL

    @property
    def hasSaved(self):
        return os.path.exists(f"{data_dir}/.links.fa")

    def save(self):
        if self.saveFile == None:
            pick = pops.pop_save()
            if pick == False:
                return
            if pick != False:
                self.saveFile = pick
        with open(f"{self.saveFile}", "wb") as file:
            pickle.dump(self.LL, file)
            file.close()

    def load(self):
        pick = pops.pop_load()
        if pick == False:
            return
        if pick != False:
            self.saveFile = pick
        with open(f"{self.saveFile}", "rb") as file:
            self.LL = pickle.load(file)
            file.close()

    def add(self, url: str):
        if url == "MAGICK":
            url = "https://youtube.com/playlist?list=PLXS7fy2pHgKch6L4xtvybDqxo4tVWAoKK"
        PL = "playlist"
        if search(PL, url):
            p = Playlist(url)
            videos = list(p.video_urls)
            for link in videos:
                self.LL.add_cur(link)
                print(f"{link} added")
        else:
            self.LL.add_cur(url)
            print(f"{url} added")

#
#    YT
#
    def download_audio(self, window):
        perfect = True
        for link in self.LL.current:
            yt = YouTube(link)
            audio = yt.streams.get_audio_only()
            destination = f"{data_dir}/Audio"
            try:
                out_file = audio.download(output_path=destination)
            except:
                err_link = f"::ERROR::\n{link}"
                self.LL.current.remove(link)
                self.LL.current.append(err_link)
                perfect = False
                continue
            base, ext = os.path.splitext(out_file)
            print(ext)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            name = os.path.split(new_file)
            self.LL.add_com(link, name[1])
            self.save()
            window.refresh()
        return perfect

    def download_video(self, window):
        perfect = True
        for link in self.LL.current:
            yt = YouTube(link)
            video = yt.streams.first()
            destination = f"{data_dir}/Videos"
            try:
                out_file = video.download(output_path=destination)
            except:
                err_link = f"::ERROR::\n{link}"
                self.LL.current.remove(link)
                self.LL.current.append(err_link)
                perfect = False
                continue
            base, ext = os.path.splitext(out_file)
            print(ext)
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
            name = os.path.split(new_file)
            self.LL.add_com(link, name[1])
            self.save()
            window.refresh()
        return perfect

#
#    GUI
#
    def makeLayout(self):
        font = sg.DEFAULT_FONT
        font = (font[0], (font[1]//2) + 1)
        sg.set_options(font = font)

        layout_left = [
        [sg.Text("Enter a link: "), sg.Input(key = "-LINK-")],
        [sg.Radio("Audio", "AV", default = True, size = (10,1), key = "-RA-"), sg.Radio("Video", "AV", default = False, size = (10,1), key = "-RV-")],
        [sg.Multiline("", size = (50, 10), key = "-console-", reroute_cprint=True, reroute_stdout=True, autoscroll = True, disabled = True)]
        ]

        list_size = (50,10)
        layout_right = [
        [sg.TabGroup([
        [sg.Tab("Current", [[sg.Listbox(self.LL.current, size = list_size, enable_events = True, key = "-LIST-")]]),
        sg.Tab("Completed", [[sg.Listbox(self.LL.completedNames(), size = list_size, enable_events = True, key = "-COMP-")]])]])]
        ]

        layout_bottom = [
        [sg.Button("Add", key = "-ADD-", bind_return_key=True), sg.Button("Save", key = "-SAVE-"), sg.Button("Load", key = "-LOAD-"), sg.Button("Clear", key = "-CLEAR-")],
        [sg.Text(""), sg.Button(image_data = base64images.DL_BTN, key = "-RUN-"),sg.Button("Quit", key = "-QUIT-"), sg.Text("")]
        ]

        layout = [
        [sg.Column(layout_left, justification = "left", pad = (5,5)), sg.Column(layout_right, justification = "right", pad = (5,5))],
        [sg.Column(layout_bottom, element_justification = "center", justification = "center", pad = (5,5))],
        [sg.StatusBar("", key = "-STAT1-", size = (50,2)), sg.StatusBar("", key = "-STAT2-", size = (50,2))]
        ]
        return layout

    def make_window(self):
        sg.theme(random.choice(sg.theme_list()))
        lo = self.makeLayout()
        win = sg.Window("Down with YT", lo, resizable = False, finalize = True, keep_on_top = True)
        return win

    def run(self):
        window = self.make_window()
        splash = pops.splash().read()
        while True:
            event, values = window.read()

            run_btn = window["-RUN-"]
            load_btn = window["-LOAD-"]
            list_box = window["-LIST-"]
            com_box = window["-COMP-"]
            stat1 = window["-STAT1-"]
            stat2 = window["-STAT2-"]

            if event in (None, "-QUIT-", sg.WIN_CLOSED):
                self.save()
                break

            if event == "-SAVE-":
                print("Save pressed")
                self.save()

            if event == "-LOAD-":
                print("Load pressed")
                self.load()

            if event == "-CLEAR-":
                print("Clear pressed")
                if self.saveFile != None:
                    choice = sg.popup_yes_no("Clear the current LinkList file?\n(*File will be saved*)")
                    if choice == "Yes":
                        self.save()
                        self.LL = LinkList()
                        self.saveFile = None
                        print("Link List is cleared")

            if event == "-ADD-":
                print("Add pressed")
                l = values["-LINK-"]
                self.add(l)

            if event == "-RUN-":
                print("Download pressed")
                if len(self.LL.current) <= 0:
                    sg.popup("HEY! Link List is EMPTY!")
                
                if pops.loginWindow() == True:
                    run_btn.update(disabled = True)
                    if values["-RA-"] == True:
                        window.perform_long_operation(self.download_audio(window), "-END-")
                    if values["-RV-"] == True:
                        window.perform_long_operation(self.download_video(window), "-END-")
                run_btn.update(disabled = False)

            if event == "-END-":
                end = values[event]
                if end == False:
                    pops.pop_oops()
                if end == True:
                    self.save()

            if event is not None:
                list_box.update(self.LL.current)
                com_box.update(self.LL.completedNames())
                if self.saveFile != None:
                    stat2.update(f"LinkList: {os.path.split(self.saveFile)[1]}")
                if self.saveFile == None:
                    stat2.update("No current LinkList file")
                print("....update....")


#
#END
if __name__ == "__main__":
    gui = LinkGui()
    gui.run()