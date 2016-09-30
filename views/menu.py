

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder


Builder.load_file('views/menu.kv')


class Menu(BoxLayout):
    def change_to_game_setup(self):
        wg = BoxLayout()
        self.parent.add_widget(wg)
        self.parent.remove_widget(self)
