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
from kivy.properties import ObjectProperty
from kivy.properties import ListProperty
from pytube import Search, YouTube
from ayoutube import aYouTube

class YTDD(DropDown):
    a_list = ListProperty(None)

    def __init__(self, **kwargs):
        super(YTDD, self).__init__(**kwargs)
    
    def on_a_list(self):
        for a in self.a_list:
            self.add_widget(a)
        

    def add_list(self, lst):
        alist = []
        for item in lst:
            appendme = ""
            if type(item) == aYouTube:
                appendme = item.title
            else:
                appendme = "__"
            btn = YTButton(text = appendme)
            alist.append(btn)
        self.a_list = alist


    @property
    def a_list(self):
        return self._a_list
    @a_list.setter
    def a_list(self, newlist):
        self._a_list = newlist



class SearchScreen(GridLayout):
    txt_in = ObjectProperty(None)
    results_label = ObjectProperty(None)
    yt_dd = ObjectProperty()
#    results = ListProperty(["Nothing","Here"])


    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        #self.yt_dd = YTDD()
        self.results = []


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
            print(tmp.title)
        self.yt_dd.add_list(self.results)


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
