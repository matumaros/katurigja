

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.world import World
from controllers.tile import Tile


class Game(FloatLayout):
    Builder.load_file('views/game.kv')

    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.tiles = {}

        self.client.bind(
            on_character_knowledge_update=self.update_player_knowledge
        )

        self.client.run()

    def move_character(self, event):
        self.client.update_character(self.player)

    def update_player_knowledge(self, ev, knowledge):
        self.update_tiles(knowledge)
        
    def update_tiles(self, tiles):
        for tile_model in tiles.values():
            tile = Tile(tile_model)
            self.tiles[(tile_model.x, tile_model.y)] = tile
            self.add_widget(tile)
