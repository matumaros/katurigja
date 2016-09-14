

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ListProperty

from controllers.tile import Tile


class World(FloatLayout):
    Builder.load_file('views/world.kv')
    real_center = ListProperty([0, 0])

    def on_real_center(self, wg, pos):
        pass

    def update_tiles(self, tiles):
        for tile_model in tiles.values():
            x, y = tile_model.x, tile_model.y
            cx, cy = self.real_center[0], self.real_center[1]
            off_x = (x - cx) * self.zoom
            off_y = (y - cy) * self.zoom
            x = self.center[0] + off_x
            y = self.center[1] + off_y

            tile = Tile(tile_model, (x, y), self.zoom)
            pos = (tile_model.x, tile_model.y)
            try:
                old_tile = self.tiles[pos]
            except IndexError:
                pass
            else:
                self.remove_children([old_tile])
            self.tiles[pos] = tile
            self.add_widget(tile)
