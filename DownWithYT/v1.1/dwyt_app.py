

import os
from pytube import YouTube, Playlist, Search
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty, ListProperty



class HomeScreen(FloatLayout):
    pass



###
#    MAIN
###
class DWYTApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        self.home_screen = HomeScreen()
        screen1 = Screen(name = "HomeScreen")
        screen1.add_widget(self.home_screen)
        
        self.screen_manager.add_widget(screen1)
        
        return self.screen_manager


if __name__ == "__main__":
    DWYTApp().run()