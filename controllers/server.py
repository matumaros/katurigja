

from peewee import Using
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.shortcuts import model_to_dict

from util.threads import thread
from models.character import Character
from models.tile import Tile


class Server:
    def __init__(self, settings={}):
        self.db = SqliteExtDatabase('saves/serversession.save')

        with open('maps/index', 'r') as f:
            maps = yaml.load(f.read())
        module = import_module(map_name)
        gmap = maps[map_name]
        self._map = getattr(module, gmap)
        running = False

        self.update_metadata(**settings)
        self.host()

    # - Serving - #
    @thread
    def host(self):
        pass

    def disconnect(self):
        pass

    # - Game Logic - #
    @thread
    def run(self):
        running = True
        while running:
            self.tick()

    def tick(self):
        pass

    def pause(self):
        running = False

    # - Metadata - #
    def update_metadata(**settings):
        pass

    # - Data - #
    def create_character(self, name, age=0, x=0, y=0, ai=True):
        with Using(self.db, [Character]):
            character = Character(db=self.db, name, age, x, y, ai)
            character.save()
        return character

    def update_character_knowledge(self, character_id):
        know = {}
        with Using(self.db, [Character, Tile]):
            character = Character.get(id=character_id)
            for i in range(-10, 11):
                for j in range(-10, 11):
                    tile = Tile.get(x=i, y=j, character_id=character_id)
                    if not tile:
                        tile = self._map.get(i, j)
                    else:
                        tile = model_to_dict(tile)
                    know[(i, j)] = tile
        return know
