

from array import array
import random

from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.widget import Widget


GROUND_TYPES = {
    'grass': [
        (26, 120, 26),
        (19, 118, 19),
        (18, 129, 30),
    ]
}
Builder.load_file('views/tile.kv')


class Tile(Widget):
    def __init__(self, model, pos, zoom):
        super().__init__()
        self.model = model
        self.update_pos(pos, zoom)
        self.update_layout()

    def update_layout(self):
        self.texture = Texture.create(size=(self.cols, self.rows))
        buf = [
            c for i in range(self.cols * self.rows)
            for c in random.choice(GROUND_TYPES[self.model.ground_type])
        ]
        arr = array('B', buf)
        self.texture.blit_buffer(arr, colorfmt='rgb', bufferfmt='ubyte')
        self.texture.mag_filter = 'nearest'
        self.texture.min_filter = 'nearest'

    def update_pos(self, pos, zoom):
        self.center = pos
        self.size = (self.default_size*zoom, self.default_size*zoom)
