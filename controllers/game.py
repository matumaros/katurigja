

from importlib import import_module

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
import yaml

from controllers.world import World


class Game(FloatLayout):
    Builder.load_file('views/game.kv')

    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client

        self.client.on_character_knowledge_update = \
            self.update_player_knowledge

        self.client.run()

    def move_character(self, event):
        self.client.update_character(self.player)

    def update_player_knowledge(self, knowledge):
        pass

    def update_player_memory(self):
        """what the player used to know, but isn't sure of now"""
        pass
