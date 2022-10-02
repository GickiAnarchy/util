import os
import kivy
import random
import time
from pytube import YouTube, Playlist, Search
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
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty, BooleanProperty
from kivy.logger import Logger
from kivy.config import Config

Config.set('graphics', 'resizable', True)


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class YT_Widget(BoxLayout):
    title = StringProperty()
    author = StringProperty()
    length = StringProperty()
    url = StringProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Logger.info("USE: YT_Widget")
        self.title = "title"
        self.author = "channel"
        self.length = "0"
        self.url = "None"

    def get_yt(self):
        if self.url != None:
            yt = YouTube(self.url)
            return yt


##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class YT_List(RecycleView):
    yt_data = ListProperty()

    def add_data(self, new_data):
        self.yt_data = [{"title":i.title, "author":i.author,"url":i.watch_url,
                         "length":str(format(i.length / 60, ".2f"))} for i in new_data]



##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class MainBox(BoxLayout):

    def do_it(self):
        txt = self.ids.search_in.text
        if txt in (None, ""):
            return False
        sch = Search(txt)
        lst = sch.results
        self.ids.yts.add_data(lst)



##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
class ScratchApp(App):
    def build(self):
        Logger.info("Start: Started App")
        return MainBox()




##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##    ##
if __name__ == "__main__":
    scr = ScratchApp()
    scr.run()