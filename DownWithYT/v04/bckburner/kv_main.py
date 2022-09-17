import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from pytube import YouTube, Search



class SearchPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        self.size_hint_x = 0.5
        self.size_hiny_y = 0.5
        self.height = 100
        self.width = 200
        self.center = (250,200)


        #    Default initialization
        self.search = None
        self.search_list = []

        #    Widget initialization
        self.add_widget(Label(text = "What would you like to search for?",
                                size_hint_y = None,
                                size_hint_x = None,
                                height = 25,
                                width = 50))    #1
        self.search_input = TextInput(multiline = False,
                                    size_hint_y = None,
                                    size_hint_x = None,
                                    height = 30,
                                    width = 100)
        self.add_widget(self.search_input)    #2
        self.add_widget(Label())    #1
        self.btn_search = Button(text = "Search",
                                    size_hint_y = None,
                                    size_hint_x = None,
                                    height = 40,
                                    width = 75)
        self.btn_search.bind(on_press = self.search_yt)
        self.add_widget(self.btn_search)    #2


    def search_yt(self, instance):
        sch_input = self.search_input.text
        if sch_input in ("", None):
            return False
        self.search = Search(sch_input)
        self.search.results()
        self.search.get_next_results()
        self.search_list = self.search.results

    def getSearchList(self):
        if not self.search_list:
            return []
        return self.search_list



class AMainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Down with YouTube"



    def build(self):
        self.screen_manager = ScreenManager()

        #    Search Screen
        self.search_screen = SearchPage()
        screen = Screen(name = "SearchPage")
        screen.add_widget(self.search_screen)
        self.screen_manager.add_widget(screen)


        return self.screen_manager



if __name__ == "__main__":
    app = AMainApp()
    app.run()
