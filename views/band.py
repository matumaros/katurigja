

from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_file('views/band.kv')


class Band(Widget):
    model = ObjectProperty(None)
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.units = []
        self.attached_to = None

    def on_model(self, ev, model):
        self.change_model(model)

    def change_model(self, model):
        self.canvas.clear()

        with self.canvas:
            Color(rgb=(1, 0, 0))
            Rectangle(pos=self.pos, size=(3, 3))
