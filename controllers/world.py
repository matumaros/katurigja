

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.tile import Tile


class World(FloatLayout):
    Builder.load_file('views/world.kv')

    def move_to(self, pos):
        off_x = (self.center[0] - pos[0]) / self.zoom
        off_y = (self.center[1] - pos[1]) / self.zoom
        cx, cy = self.parent.character.x, self.parent.character.y
        self.parent.set_player_path([(cx + off_x, cy + off_y)])

    def update_character(self, character):
        pass

    def update_tiles(self, tiles):
        for tile_model in tiles.values():
            x, y = tile_model.x, tile_model.y
            cx, cy = self.parent.character.x, self.parent.character.y
            off_x = (x - cx) * self.zoom
            off_y = (y - cy) * self.zoom
            x = self.center[0] + off_x
            y = self.center[1] + off_y

            tile = Tile(tile_model, (x, y), self.zoom)
            self.tiles[(tile_model.x, tile_model.y)] = tile
            self.add_widget(tile)
