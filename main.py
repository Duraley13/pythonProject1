from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (79/255, 79/255, 79/255, 1)

class ParserApp(App):
    def build(self):

        label = Label(text="Hello, World")
        label.color = (1, 1, 1, 1)

        return label

if __name__ == "__main__":
    ParserApp().run()