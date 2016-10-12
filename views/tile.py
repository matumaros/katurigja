

import random

from kivy.lang import Builder
from kivy.uix.widget import Widget


GROUND_TYPES = {
    'grass': [
        (26, 120, 26),
        (19, 118, 19),
        (18, 125, 30),
    ],
}
BUILDING_TYPES = {
    'roof': [
        (59, 46, 49),
        (62, 42, 45),
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
