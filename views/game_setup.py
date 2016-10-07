

import yaml
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


Builder.load_file('views/game_setup.kv')


class GameSetup(Screen):
    def __init__(self, last_screen, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_screen = last_screen
        self.client = client
        self.settings = {}
        with open('maps/index', 'r') as f:
            self.maps = yaml.load(f.read())
        self.map_selection.values = self.maps.keys()
        self.map_selection.text = 'flat_grassland'

    def on_settings_change(self, key, value):
        self.settings[key] = value

    def go_back(self):
        self.parent.current = self.last_screen

    def start_game(self):
        self.client.update_settings(**self.settings)
        self.parent.current = 'game'
