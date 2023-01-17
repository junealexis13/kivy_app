#main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty

class MyScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_list = [1, 2, 3, 4, 5]
        scroll_view = ScrollView(size_hint=(1, None), size=(self.width, self.height))
        recycle_view = RecycleView(size_hint=(1, None), size=(self.width, self.height))
        recycle_view.data = self.my_list
        recycle_view.viewclass = 'Label'
        recycle_view.layout = GridLayout(cols=1, size_hint_y=None)
        recycle_view.layout.bind(minimum_height=recycle_view.layout.setter('height'))
        scroll_view.add_widget(recycle_view)
        self.add_widget(scroll_view)

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyScreen(name='my_screen'))
        return sm

if __name__ == '__main__':
    MainApp().run()
