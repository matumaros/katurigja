

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.world import World


class Game(FloatLayout):
    Builder.load_file('views/game.kv')

    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.set_player(client.character)

        self.client.bind(
            on_character_knowledge_update=self.update_player_knowledge
        )
        self.client.bind(
            on_character=self.set_player
        )

        self.client.run()

    def set_player(self, player):
        self.character = player

    def set_player_path(self, path):
        self.client.set_player_path(path)

    def move_player_to(self, x, y):
        self.client.move_player_to(x, y)

    def update_player_knowledge(self, ev, knowledge):
        self.world.update_tiles(knowledge)
