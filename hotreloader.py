from kaki import app as kApp
from kivy.app import App
from kivy.core.window import Window
from kivy.factory import Factory

Window.size = (412, 732)
Window.clearcolor = (63/255, 22/255, 81/255, 1.0)

class ScrManager(kApp, App):
    CLASSES = {
        "ScrManager" : "main"
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]

    def build_app(self, *args):
        return Factory.UI()


ScrManager().run() 