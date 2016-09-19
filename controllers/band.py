

from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle

Builder.load_file('views/band.kv')


class Band(Widget):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.units = []
        self.attached_to = None

        self.update()

    def update(self):
        with self.canvas:
            Color(rgb=(1, 0, 0))
            Rectangle(pos=self.pos, size=(3, 3))
