

import os
import json
from pytube import YouTube, Playlist, Search
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty, ListProperty



class YTScreenManager(ScreenManager):
    home_screen       =     ObjectProperty(None)
    file_screen       =     ObjectProperty(None)

    def __init__(self, **kwargs):
        super(YTScreenManager, self).__init__(**kwargs)

        self.home_screen = HomeScreen()
        self.add_widget(self.home_screen)
        self.file_screen = FileScreen()
        self.add_widget(self.file_screen)


class HomeScreen(Screen):
    pass


class FileScreen(Screen):
    ''' FileScreen:
        -Screen to show downloaded songs/videos, saved lists, and load lists.
    '''
    file_list = ListProperty(None)

    def __init__(self, **kwargs):
        super(FileScreen, self).__init__(**kwargs)
        self.saved_lists = []
        self.songs = []
        self.videos = []

    def read_directory(self, local_dir):
        for file in os.listdir(local_dir):
            if file.endswith(".mp3"):
                self.songs.append(file)
            if file.endswith(".mp4"):
                self.videos.append(file)
            if file.endswith(".dwyt"):
                self.saved_lists.append(file)
            self.file_list.append(file)

    def save_list(self,fname,ytlist):
        overwrite = True
        if os.path.isfile(fname):
            if overwrite == False:
                name, ext = os.path.splitext(fname)
                fname = name + "(c)" + ext
        with open(fname, "w") as file:
            for itm in ytlist:
                file.write(itm.watch_url)
            file.close()

    def load_list(self,fname):
        url_list = []
        yt_list = []
        with open(fname, "r") as file:
            url_list = file.readlines()
            file.close()
        for url in url_list:
            tyt = YouTube(url)
            yt_list.append(tyt)
            print(f"{tyt.title} loaded")
        return yt_list


class RV(RecycleView):
    data_list = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data_list = [{"text":str(i)} for i in range(2)]

    def add(self, alist):
        self.data_list = [{"text":f"{item.title}"} for item in alist]
        self.refresh_from_data()


class YT_List(FloatLayout):

    def __init__(self, **kwargs):
        super(YT_List, self).__init__(**kwargs)
        #self.ids.search_btn.bind(on_press = self.doSearch)

    def doSearch(self):
        txt = self.ids.txt_input.text
        if txt in ("", None, "..."):
            return False
        search = Search(txt)
        lst = search.results
        self.ids.rv.add(lst)


###
#    MAIN
###
class DWYTApp(App):
    def build(self):
        return YT_List()


if __name__ == "__main__":
    DWYTApp().run()