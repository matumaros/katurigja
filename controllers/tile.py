

import random

from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import InstructionGroup
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


class Tile(Widget):
    def __init__(self, model, pos, zoom):
        super().__init__()
        self.rectangles = []
        self.model = model
        self.update_pos(pos, zoom)
        self.update_layout()

    def update_layout(self):
        self.canvas.clear()
        self.rectangles.clear()

        for x in range(self.cols):
            for y in range(self.rows):
                instr = InstructionGroup()
                
                color = random.choice(GROUND_TYPES[self.model.ground_type])
                instr.add(Color(rgb=color))

                width = self.width / self.cols
                height = self.height / self.rows
                rectangle = Rectangle(
                    pos=(self.pos[0]+x*width, self.pos[1]+y*height),
                    size=(width, height),
                )
                instr.add(rectangle)
                self.rectangles.append(rectangle)

                self.canvas.add(instr)

    def update_pos(self, pos, zoom):
        off_x, off_y = self.pos[0] - pos[0], self.pos[1] - pos[1]
        for rect in self.rectangles:
            rect.pos = (rect.pos[0]+off_x, rect.pos[1]+off_y)
        self.pos = pos
        self.size = (self.default_size*zoom, self.default_size*zoom)
