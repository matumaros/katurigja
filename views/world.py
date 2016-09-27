

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ListProperty

from views.tile import Tile
from views.band import Band


class World(FloatLayout):
    Builder.load_file('views/world.kv')
    real_center = ListProperty([0, 0])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind(size=self.on_real_center)

    def on_real_center(self, wg, pos):
        for tile in list(self.tiles.values()):
            x, y = tile.model.x, tile.model.y
            tile.update_pos(self.real_to_wg(x, y), self.zoom)

    def update_band(self, band_model):
        pos = self.real_to_wg(*band_model.pos)
        try:
            band = self.bands[band_model.id]
        except KeyError:
            band = Band(band_model, pos=pos)
            self.bands[band_model.id] = band
            self.add_widget(band)
        else:
            band.pos = pos
            band.change_model(band_model)
            self.remove_widget(band)
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
