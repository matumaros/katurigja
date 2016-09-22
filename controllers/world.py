

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ListProperty

from controllers.tile import Tile
from views.band import Band


class World(FloatLayout):
    Builder.load_file('views/world.kv')
    real_center = ListProperty([0, 0])

    def on_real_center(self, wg, pos):
        for tile in self.tiles.values():
            x, y = tile.model.x, tile.model.y
            tile.x, tile.y = self.real_to_wg(x, y)

    def update_bands(self, bands):
        for band_model in bands.values():
            pos = self.real_to_wg(*band_model.pos)
            try:
                band = self.bands[band_model.id]
            except KeyError:
                band = Band(band_model, pos=pos)
            else:
                band.pos = pos
                band.model = model
                self.bands[band_model.id] = band
                self.add_widget(band)

    def update_tiles(self, tiles):
        for tile_model in tiles.values():
            pos = (tile_model.x, tile_model.y)

            try:
                old_tile = self.tiles[pos]
            except KeyError:
                x, y = self.real_to_wg(tile_model.x, tile_model.y)
                tile = Tile(tile_model, (x, y), self.zoom)
                self.tiles[pos] = tile
                self.add_widget(tile)
            else:
                old_tile.model = tile_model
                old_tile.update_layout()

    def real_to_wg(self, x, y):
        cx, cy = self.real_center[0], self.real_center[1]
        off_x = (x - cx) * self.zoom
        off_y = (y - cy) * self.zoom
        x = self.center[0] + off_x
        y = self.center[1] + off_y
        return x, y
