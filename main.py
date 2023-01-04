from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation
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


class Menu_Stats(Screen):
    pass


class Menu_Chars(Screen):
    pass

class ScrManager(ScreenManager):
    pass

kv = Builder.load_file("random.kv")

class RandomApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    RandomApp().run()