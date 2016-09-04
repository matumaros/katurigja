

from time import time
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

        self.characters = {}
        self.tiles = {}

        self.update_metadata(**settings)

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
        self.running = False

    # - Metadata - #
    def update_metadata(self, **settings):
        pass

    # - Data - #
    def create_character(self, name, age=0, x=0, y=0, ai=True):
        cid = uuid.uuid4()
        character = {
            'info': {
                'id': cid, 'name': name, 'age': age, 'x': x, 'y': y, 'ai': ai,
            },
            'characters': {},
            'tiles': {},
        }
        self.characters[cid] = character
        return character

    def update_character_knowledge(self, character_id):
        know = {}
        character = self.characters[character_id]
        for i in range(-5, 6):
            for j in range(-5, 6):
                i += character['info']['x']
                j += character['info']['y']

                fact = self.tiles.get((i, j))
                if not fact:
                    fact = self._map.get(i, j)
                    self.tiles[(i, j)] = fact

                self.characters[character_id]['tiles'][(i, j)] = fact
                know = fact
        return know
