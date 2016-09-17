
from collections import namedtuple

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


## - from controllers.tile import Tile - ##
from array import array
import random

from kivy.graphics.texture import Texture
from kivy.lang import Builder
from kivy.uix.widget import Widget


GROUND_TYPES = {
    'grass': [
        (14, 167, 67),
        (10, 104, 0),
        (37, 137, 25),
    ]
}
Builder.load_string('''
#:kivy 1.9.1

<Tile>:
    size_hint: (None, None)
    cols: 8
    rows: 8
    texture: None
    default_size: 1

    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            texture: self.texture

''')


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

    def update_pos(self, pos, zoom):
        self.pos = pos
        self.size = (self.default_size*zoom, self.default_size*zoom)
## - import end - ##


Builder.load_string('''
#:kivy 1.9.1

<FloatLayout>:
    canvas:
        Color:
            rgb: 0, 103, 67
        Rectangle:
            pos: self.pos
            size: self.size

''')

zoom = 32
Model = namedtuple(
    'Tile',
    ['x', 'y', 'altitude', 'ground_type', 'settlement_size', 'resource']
)
    

class Test(App):
    view = FloatLayout()

    def __init__(self):
        super().__init__()
        self.view.bind(on_touch_down=self.add_tile)

    def add_tile(self, wg, ev):
        print('add')
        x, y = ev.pos
        model = Model(0, 0, 0, 'grass', 0, None)
        tile = Tile(model, (x, y), zoom)
        self.view.add_widget(tile)

    def build(self):
        return self.view

test = Test()
for i in range(9):
    for j in range(9):
        x, y = i*zoom, j*zoom
        model = Model(i, j, 0, 'grass', 0, None)
        tile = Tile(model, (x, y), zoom)
        test.view.add_widget(tile)
test.run()
