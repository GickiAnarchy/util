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
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty, BooleanProperty




class YT_Widget(Widget):
    yt = None
    has_yt = BooleanProperty(False)

    def add_yt(self, yt_obj):
        if isinstance(yt_obj, YouTube):
            self.yt = yt_obj
            self.has_yt = True

    def on_has_yt(self, instance, value):
        print(f"\n***********\n{type(value)}\n***********\n")
        if self.has_yt:
            self.ids.yt_title.text = self.yt.title
            self.ids.yt_author.text = self.yt.author
            self.ids.yt_length.text = str(format(self.yt.length / 60, ".2f"))
    
    def get_yt(self):
            self.ids.yt_btn_img.source = "images/red_btn.png"
            time.sleep(1.5)
            if not self.has_yt:
                search = Search("fatheranarchy")
                res = search.results
                iyt = random.choice(res)
                self.add_yt(iyt)
            self.ids.yt_btn_img.source = "images/grn_btn.png"
            return self.yt




class ScratchApp(App):
    def build(self):
        return YT_Widget()




if __name__ == "__main__":
    scr = ScratchApp()
    scr.run()