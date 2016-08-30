

from . import Procedually


class FlatGrassland(Procedually):
    def build(self, x, y):
        return {
            'ground_type': 'grass',
        }
