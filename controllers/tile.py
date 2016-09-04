

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
    def __init__(self, model):
        super().__init__(pos=(model.x, model.y), size=(8, 8))
        self.update_layout(model)

    def update_layout(self, model):
        self.model = model
        self.clear_widgets()
        color = random.choice(GROUND_TYPES[model.ground_type])

        for i in range(self.cols*self.rows):
            self.add_widget(TilePixel(color))


class TilePixel(Widget):
    def __init__(self, color):
        super().__init__()
        self.set_color(color)

    def set_color(self, color):
        self.canvas.add(Color(*color))
