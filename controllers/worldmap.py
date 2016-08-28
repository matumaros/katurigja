

from kivy.uix.boxlayout import BoxLayout

from models.worldmap import WorldMapModel

class WorldMap(BoxLayout):
    def __init__(self):
        super().__init__()
        self.model = WorldMapModel()

    def update(x, y, tile):
        self.model.update(x, y, tile)         
