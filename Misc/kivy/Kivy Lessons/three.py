''' Clock event schedule and trigger '''
import kivy
import time

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.trigger = Clock.create_trigger(self.talker)
        self.cols = 2
        self.add_widget(Label(text = "User Name"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "password"))
        self.password = TextInput(password = True, multiline = False)
        self.add_widget(self.password)

    def talker(self, dt):
        self.username.text = "bobobobob"
        self.password.password = False
        self.password.text = "01234"

class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.ls = LoginScreen()
        self.t = Clock.schedule_once(self.ls.trigger, 10)

    def build(self):
        return self.ls

    def run(self):
        self.t()
        super().run()


if __name__ == "__main__":
    r = MyApp()
    r.run()