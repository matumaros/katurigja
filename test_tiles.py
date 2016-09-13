
from collections import namedtuple

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


## - from controllers.tile import Tile - ##
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
Builder.load_string('''
#:kivy 1.9.1

<Tile>:
    cols: 3
    rows: 3
    size_hint: (None, None)
    default_size: 1

<TilePixel>:
    canvas:
        Color:
            rgb: self.color
        Rectangle:
            pos: self.pos
            size: self.size

''')


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
    def __init__(self, color):
        super().__init__()
        self.set_color(color)

    def set_color(self, color):
        self.color = color
        # self.canvas.add(self.color)
## - import end - ##


zoom = 32
Model = namedtuple(
    'Tile',
    ['x', 'y', 'altitude', 'ground_type', 'settlement_size', 'resource']
)

class Test(App):
    view = FloatLayout()
    def build(self):
        return self.view

test = Test()
for i in range(2):
    for j in range(2):
        x, y = i*zoom, j*zoom
        model = Model(i, j, 0, 'grass', 0, None)
        tile = Tile(model, (x, y), zoom)
        test.view.add_widget(tile)
test.run()
