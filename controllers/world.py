

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from models.world import World as WorldModel


class World(FloatLayout):
    Builder.load_file('views/world.kv')
