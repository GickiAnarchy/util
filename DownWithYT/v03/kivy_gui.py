from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        #add widgets to window

        #Image widget
        self.img = Image(source="/images/red_light.png")
        self.window.add_widget(self.img)
        
        #Label widget
        self.greeting = Label(text = "Whats your name?")
        self.window.add_widget(self.greeting)
        
        #TextInput widget
        self.textinput = TextInput(multiline = False)
        self.window.add_widget(self.textinput)
        
        #Button widget
        self.button = Button(text = "GREET")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self, instance):
        self.greeting.text = "Hello" + self.textinput.text + "!"



if __name__ == "__main__":
    SayHello().run()
    