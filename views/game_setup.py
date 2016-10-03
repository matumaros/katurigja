

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('views/game_setup.kv')


class GameSetup(Screen):
    def __init__(self, last_screen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_screen = last_screen

    def go_back(self):
        self.parent.current = self.last_screen

    def start_game(self):
        self.parent.current = 'game'
