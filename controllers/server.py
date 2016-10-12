

from importlib import import_module
from math import sqrt
import os
from time import time
import uuid

from kivy.clock import Clock
import yaml

from util.threads import thread
from controllers.band import Band
from models.band import Band as BandModel
from models.character import Character


class Server:
    def __init__(self, settings={}):
        super().__init__()

        self.running = False
        self.TPS = 10
        self.local_client = None
        self.players = {}

        with open('maps/index', 'r') as f:
            self.maps = yaml.load(f.read())
        self._map = None

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
        assert self._map
        self.running = True
        self.tick(first=True)
        self._run()

    def _run(self):
        if self.running:
            Clock.schedule_once(lambda dt: self._run(), 1/self.TPS)
            self.tick()

    def dispatch(self, player_id, knowledge):
        player = self.players[player_id]
        try:
            player.update_character_knowledge(knowledge)
        except AttributeError:
            pass # Try connecting to networ client

    def tick(self, first=False):
        # dispatch game events
        for id in self.players:
            char = self.characters[id]
            band = self.bands[char.band.id]
            band.update()
            lx, ly = char.band.last_pos
            x, y = char.band.pos
            if first or (int(x), int(y)) != (int(lx), int(ly)):
                self.update_tiles(character=char)

        if self.local_client:
            self.local_client.tick(first=first)

    def pause(self):
        self.running = False

    def update_tiles(self, character):
        x, y = character.band.pos
        x, y = int(x), int(y)
        distance = 10

        tiles = {}
        for i in range(-distance, distance+1):
            i += x
            for j in range(-distance, distance+1):
                j += y
                assert all(map(lambda i: isinstance(i, int), (i, j)))

                fact = self.tiles.get((i, j))
                if not fact:
                    fact = self._map.get(i, j)
                    self.tiles[(i, j)] = fact

                if (i, j) not in character.tiles:
                    character.tiles[(i, j)] = fact
                    tiles[(i, j)] = fact
        self.dispatch(character.id, {'tiles': tiles})

    # - Calls - #
    def update_metadata(self, **settings):
        try:
            map_name = settings['map_name']
        except KeyError:
            pass
        else:
            module = import_module('maps.' + map_name)
            gmap = self.maps[map_name]
            self._map = getattr(module, gmap)()

    def set_band_path(self, id, path):
        # Inform other players about change
        self.bands[id].set_path(path)

    def create_character(
            self, name,
            x=0, y=0, band=None, age=0, player=False, speed=0.015):
        cid = uuid.uuid4()
        if player:
            self.players[cid] = player
        bid = uuid.uuid4()
        character = Character(
            cid, name, age, band, not bool(player), speed, {}, {}, {}
        )
        self.characters[cid] = character

        if not band:
            band = BandModel(
                bid, name + "'s Band", character, (x, y), (x, y), speed,
                {character.id: character}, {}
            )
            character.band = band
            self.bands[bid] = Band(model=band)
        return character
