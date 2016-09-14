

import random

from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ListProperty


GROUND_TYPES = {
    'grass': [
        (14/255, 167/255, 67/255),
        (10/255, 104/255, 0/255),
        (37/255, 137/255, 25/255),
    ]
}
Builder.load_file('views/tile.kv')


class Tile(GridLayout):
    def __init__(self, model, pos, zoom):
        super().__init__()
        self.model = model
        self.update_layout()
        self.update_pos(pos, zoom)

    def update_layout(self):
        self.clear_widgets()
        color = random.choice(GROUND_TYPES[self.model.ground_type])

        for i in range(self.cols*self.rows):
            pixel = TilePixel(color)
            self.add_widget(pixel)

    def update_pos(self, pos, zoom):
        self.pos = pos
        self.size = (self.default_size*zoom, self.default_size*zoom)


class TilePixel(Widget):
    color = ListProperty([1, 1, 1, 1])

    def __init__(self, color):
        super().__init__()
        self.color = color
