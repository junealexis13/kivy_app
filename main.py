from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

import re

from backend import backend

Window.size = (412, 732)
Window.clearcolor = (63/255, 22/255, 81/255, 1.0)


class WelcomeScreen(Screen):
    def on_press_animation(self, *args):
        self.ids.splash_image.opacity = 0.5
    def on_release_animation(self, *args):
        self.ids.splash_image.opacity = 1

class MainMenu(Screen):
    def on_press_animation(self, *args):
        self.ids.back_image.opacity = 0.5
    def on_release_animation(self, *args):
        self.ids.back_image.opacity = 1

    def menu_animate(self, widget, *args):
        menu_anim = Animation(
            background_color = (248/255,159/255,91/255,0.25),
            duration = 0.25
        ) 
        menu_anim += Animation(background_color = (248/255,159/255,91/255,0), duration = 0.5)
        menu_anim.start(widget)


playerUser = backend.PlayerUser()
 
class Menu_Stats(Screen):
    pass

class Menu_Chars(Screen):
    pass

class Menu_Resources(Screen):
    pass

class Menu_Userprofile(Screen):
    rd = open("backend/current_userprofile.txt","r")
    content = rd.read()
    id = re.findall(r"name:.*", content, re.MULTILINE)[0].replace("name: ","")
    uid = re.findall(r"uid:.*", content, re.MULTILINE)[0].replace("uid: ","")
    # ltoken = re.findall(r"ltoken:.*", content, re.MULTILINE)[0].replace("ltoken: ","")
    # ltuid = re.findall(r"ltuid:.*", content, re.MULTILINE)[0].replace("ltuid: ","")
    rd.close()

class ScrManager(ScreenManager):
    pass

kv = Builder.load_file("random.kv")

class RandomApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    RandomApp().run()