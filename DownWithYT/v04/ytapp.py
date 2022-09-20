#filename: ytapp.py

import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from pytube import Search, YouTube
from ayoutube import aYouTube


class SearchScreen(GridLayout):
    txt_in = ObjectProperty(None)
    res_list = ListProperty(None)

    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.results = []
        self.res_list = []

    def do_search(self):
        user_input = self.txt_in.text
        search = Search(user_input)
        search.results
        search.get_next_results()
        res = search.results
        self.results.clear()
        for r in res:
            tmp = aYouTube(r)
            self.results.append(tmp)
        self.res_list = self.results

    @property
    def results(self):
        return self._results
    @results.setter
    def results(self, newres):
        self._results = newres





class YTApp(App):
    def build(self):
        return SearchScreen()
#        self.screen_man = ScreenManager()
#        self.search_screen = SearchScreen()
#        screen = Screen(name = "SearchPage")
#        screen.add_widget(self.search_screen)
#        self.screen_man.add_widget(screen)
#        return self.screen_man



if __name__ == "__main__":
    YTApp().run()
