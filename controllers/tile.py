

import random

from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


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
            self.add_widget(TilePixel(color))

    def update_pos(self, pos, zoom):
        self.pos = pos
        self.size = (self.default_size*zoom, self.default_size*zoom)


class TilePixel(Widget):
    def __init__(self, color):
        super().__init__()
        self.set_color(color)

    def set_color(self, color):
        self.canvas.add(Color(*color))
