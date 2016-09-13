

from . import Procedually
from models.tile import Tile


class FlatGrassland(Procedually):
    def build(self, x, y):
        return Tile(
            x=x,
            y=y,
            altitude=0,
            ground_type='grass',
            settlement_size=0,
            resource=None,
        )
