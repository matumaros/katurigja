

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('views/menu.kv')


class Menu(Screen):
    def change_to_game_setup(self):
        self.parent.current = 'game_setup'
