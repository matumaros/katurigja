

from time import time
import os
from importlib import import_module
import uuid

import yaml

from util.threads import thread
from models.character import Character
from models.tile import Tile


class Server:
    def __init__(self, settings={}):
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
        character = Character(cid, name, age, x, y, ai, {}, {})
        self.characters[cid] = character
        return character

    def update_character_knowledge(self, character_id):
        know = {}
        character = self.characters[character_id]
        for i in range(-5, 6):
            for j in range(-5, 6):
                i += character.x
                j += character.y

                fact = self.tiles.get((i, j))
                if not fact:
                    fact = self._map.get(i, j)
                    self.tiles[(i, j)] = fact

                self.characters[character_id].tiles[(i, j)] = fact
                know[(i, j)] = fact
        return know
