import re




from kivy.app import App
from kivy.lang import Builder

kv = '''
#:import Button kivy.uix.button.Button
BoxLayout:
    on_parent:
        if not self.children: [self.add_widget(Button(text=str(i))) for i in range(10)]
'''

class LoopApp(App):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":

    LoopApp().run()