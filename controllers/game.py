

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.world import World


class Game(FloatLayout):
    Builder.load_file('views/game.kv')

    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client

        self.client.bind(
            on_character_knowledge_update=self.update_player_knowledge
        )

        self.client.run()

    def move_character(self, event):
        self.client.update_character(self.player)

    def update_player_knowledge(self, knowledge):
        print(knowledge)
