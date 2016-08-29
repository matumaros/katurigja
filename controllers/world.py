

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


class World(FloatLayout):
    Builder.load_file('views/world.kv')
