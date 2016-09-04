

from time import time
import os
from importlib import import_module
import uuid

from kivy.clock import Clock
from kivy.event import EventDispatcher
import yaml

from util.threads import thread
from models.character import Character
from models.tile import Tile


class Server(EventDispatcher):
    def __init__(self, settings={}):
        self.register_event_type('on_tick')
        super().__init__()

        self.running = False
        self.tps = 1

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
    def run(self):
        self.running = True
        self._run()

    def _run(self):
        self.tick()
        if self.running:
            Clock.schedule_once(lambda dt: self._run(), 1/self.tps)

    @thread
    def tick(self):
        self.dispatch('on_tick')

    def pause(self):
        self.running = False

    # - Default Events - #
    def on_tick(self):
        return

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

                if (i, j) not in self.characters[character_id].tiles:
                    self.characters[character_id].tiles[(i, j)] = fact
                    know[(i, j)] = fact
        return know
