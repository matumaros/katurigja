

from . import Procedually
from models.tile import Tile


class FlatGrassland(Procedually):
    def build(self, x, y):
        return Tile(
            x=0,
            y=0,
            altitude=0,
            ground_type='grass',
        )
