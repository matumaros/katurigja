

import os
from importlib import import_module
import uuid

from peewee import Using
from playhouse.sqlite_ext import SqliteExtDatabase
from playhouse.shortcuts import model_to_dict
import yaml

from util.threads import thread
from models.character import Character
from models.tile import Tile


class Server:
    def __init__(self, settings={}):
        try:
            os.remove('saves/serversession.save')
        except OSError:
            pass
        self.db = SqliteExtDatabase('saves/serversession.save')
        self.db.connect()
        with Using(self.db, [Character, Tile]):
            self.db.create_tables([Character, Tile])

        running = False

        with open('maps/index', 'r') as f:
            maps = yaml.load(f.read())
        map_name = settings['map_name']
        module = import_module('maps.' + map_name)
        gmap = maps[map_name]
        self._map = getattr(module, gmap)()

        self.update_metadata(**settings)

    def __del__(self):
        print('database closed')
        self.db.close()

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
    def update_metadata(self, **settings):
        pass

    # - Data - #
    def create_character(self, name, age=0, x=0, y=0, ai=True):
        with Using(self.db, [Character]):
            character = Character(
                uuid=uuid.uuid4(), name=name, age=age, x=x, y=y, ai=ai,
            )
            character.save()
        return character

    def update_character_knowledge(self, character_id):
        know = {}
        with Using(self.db, [Character, Tile]):
            character = Character.get(uuid=character_id)
            for i in range(-10, 11):
                for j in range(-10, 11):
                    i += character.x
                    j += character.y

                    try:
                        tile = Tile.get(x=i, y=j, character_uuid='')
                    except Tile.DoesNotExist:
                        tile = self._map.get(i, j)
                        new_fact = Tile(uuid=uuid.uuid4(), **tile)
                        new_fact.save()
                    else:
                        tile = model_to_dict(tile)
                    tile.update({
                        'uuid': uuid.uuid4(),
                        'character_id': character_id,
                    })
                    new_knowledge = Tile(**tile)
                    new_knowledge.save()
                    know[(i, j)] = tile
        return know
