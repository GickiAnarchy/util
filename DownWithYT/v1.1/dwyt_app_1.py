

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
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty, ListProperty



class YTScreenManager(ScreenManager):
    home_screen = ObjectProperty(None)
    file_screen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(YTScreenManager, self).__init__(**kwargs)

        self.file_screen = FileScreen()
        self.add_widget(self.file_screen)
        self.home_screen = HomeScreen()
        self.add_widget(self.home_screen)


class HomeScreen(Screen):
    pass


class FileScreen(Screen):
    ''' FileScreen:
        -Screen to show downloaded songs/videos, saved lists, and load lists.
    '''
    file_list = ListProperty(None)
    
    def read_directory(self, local_dir):
        self.file_list = []
        for file in os.listdir(local_dir):
            if file.endswith(".mp3"):
                pass    #TODO: handle songs
            if file.endswith(".mp4"):
                pass    #TODO: handle videos
            if file.endswith(".dwyt"):
                pass    #TODO: handle saved lists
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
        with open(fname, "r") as file:
            for line in file.read():


#
#
class YTList(Widget):
    pass




###
#    MAIN
###
class DWYTApp(App):
    screen_manager = ObjectProperty(None)

    def build(self):
        self.screen_manager = YTScreenManager()
        self.screen_manager.add_widget(HomeScreen())
        self.screen_manager.add_widget(FileScreen())
        
        return self.screen_manager


if __name__ == "__main__":
    DWYTApp().run()