

from importlib import import_module
from math import sqrt
import os
from time import time
import uuid

from kivy.clock import Clock
from kivy.event import EventDispatcher
import yaml

from util.threads import thread
from models.band import Band
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
        self.bands = {}
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

    def set_band_path(self, id, path):
        self.bands[id].path = path

    # - Data - #
    def create_character(
            self, name, x=0, y=0, band=None, age=0, ai=True, speed=1):
        cid = uuid.uuid4()
        bid = uuid.uuid4()
        character = Character(
            cid, name, age, band, ai, speed, {}, {}
        )
        self.characters[cid] = character

        if not band:
            band = Band(
                bid, name + "'s Band", character, (x, y), (x, y), speed,
                {character.id: character}, {}
            )
            character.band = band
            self.bands[bid] = band
        return character

    def update_character(self, character):
        goal = character.path[0]
        x, y = character.x, character.y
        a = abs(x - goal[0])**2
        b = abs(y - goal[1])**2
        distance = sqrt(a + b)
        factor = character.speed / distance
        dx, dy = goal[0] * factor, goal[1] * factor
        character.last_pos = (x, y)
        character.x += dx
        character.y += dy

    def update_character_knowledge(self, character_id):
        know = {}
        character = self.characters[character_id]
        lx, ly = character.band.last_pos
        x, y = character.band.pos
        if (round(x), round(y)) == (round(lx), round(ly)):
            return know
        distance = 1
        for i in range(-distance, distance+1):
            for j in range(-distance, distance+1):
                i += round(x)
                j += round(y)
                assert all(map(lambda i: isinstance(i, int), (i, j)))

                fact = self.tiles.get((i, j))
                if not fact:
                    fact = self._map.get(i, j)
                    self.tiles[(i, j)] = fact

                if (i, j) not in self.characters[character_id].tiles:
                    self.characters[character_id].tiles[(i, j)] = fact
                    know[(i, j)] = fact
        return know
