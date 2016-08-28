

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.worldserver import WorldServer


class World(FloatLayout):
    Builder.load_file('views/world.kv')
    def __init__(self, server=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not server:
            self.server = WorldServer()
        else:
            self.server = server
