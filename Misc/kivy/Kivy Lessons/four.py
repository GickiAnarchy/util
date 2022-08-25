''' Introducing the kv language i.e. four.kv '''
import random
import kivy
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import  Widget


class FourWidget(Widget):
    pass


class FourApp(App):

    def build(self):
        chs = [0,1,2,3]
        r = random.choice(chs)
        if r in (0,1):
            return Label()
        if r in (2,3):
            return FourWidget()

if __name__ == "__main__":
    FourApp().run()