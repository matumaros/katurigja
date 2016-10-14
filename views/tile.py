

import random

from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget


GROUND_TYPES = {
    'grass': [
        (26 / 255, 120 / 255, 26 / 255, 1),
        (19 / 255, 118 / 255, 19 / 255, 1),
        (18 / 255, 125 / 255, 30 / 255, 1),
    ],
}
BUILDING_TYPES = {
    'roof': [
        (59 / 255, 46 / 255, 49 / 255, 1),
        (62 / 255, 42 / 255, 45 / 255, 1),
    ],
}

Builder.load_file('views/tile.kv')


class Tile(Widget):
    def __init__(self, model, pos, zoom):
        super().__init__()
        self.model = model
        self.update_pos(pos, zoom)
        self.update_layout()

    def update_layout(self):
        if self.model.settlement:
            self.color = random.choice(BUILDING_TYPES['roof'])
        else:
            self.color = random.choice(GROUND_TYPES[self.model.ground_type])

    def update_pos(self, pos, zoom):
        self.center = pos
        self.size = (self.default_size*zoom, self.default_size*zoom)
