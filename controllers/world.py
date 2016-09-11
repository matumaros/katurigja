

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.tile import Tile


class World(FloatLayout):
    Builder.load_file('views/world.kv')

    def move_to(self, pos):
        x = (self.center[0] - pos[0]) / self.zoom
        y = (self.center[1] - pos[1]) / self.zoom
        cx, cy = self.parent.character.x, self.parent.character.y
        self.parent.set_player_path([(cx + x, cy + y)])

    def update_character(self, character):
        pass

    def update_tiles(self, tiles):
        for tile_model in tiles.values():
            tile = Tile(tile_model, 1)
            self.tiles[(tile_model.x, tile_model.y)] = tile
            self.add_widget(tile)
