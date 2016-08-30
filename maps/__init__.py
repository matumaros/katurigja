

from peewee import Using
from playhouse.sqlite_ext import SqliteExtDatabase

from models.tile import Tile


class PreMade:
    def __init__(self, map_path):
        self._db = SqliteExtDatabase(map_path)


class PreGenerated(PreMade):
    def __init__(self):
        super().__init__(self, map_path='maps/last_generated.map'):
        tiles = self.build()
        with Using(self._db, [Tile]):
            for tile in tiles:
                tile = Tile(**tile)
                tile.save()

    def get(self, x, y):
        with Using(self._db, [Tile]):
            tile = Tile.get(x == x and y == y)
        return tile._data

    def build(self):
        return []


class Procedually:
    def get(self, x, y):
        return self.build(x, y)

    def build(self, x, y):
        return {}
