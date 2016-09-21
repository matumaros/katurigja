

from importlib import import_module
from math import sqrt
import os
from time import time
import uuid

from kivy.clock import Clock
import yaml

from util.threads import thread
from models.band import Band
from models.character import Character
from models.tile import Tile


class Server:
    def __init__(self, settings={}):
        super().__init__()

        self.running = False
        self.tps = 1
        self.players = {}

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

    def dispatch(self, player_id, knowledge):
        player = self.players[player_id]
        try:
            player.update_character_knowledge(knowledge)
        except AttributeError:
            pass # Try connecting to networ client

    @thread
    def tick(self):
        # dispatch game events
        for player in self.players:
            self.update_band_position(leader_id=player)

    def pause(self):
        self.running = False

    def update_band_position(self, leader_id):
        tiles = {}
        character = self.characters[leader_id]
        lx, ly = character.band.last_pos
        x, y = character.band.pos
        if (round(x), round(y)) == (round(lx), round(ly)):
            return
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

                if (i, j) not in character.tiles:
                    character.tiles[(i, j)] = fact
                    tiles[(i, j)] = fact
        self.dispatch(leader_id, {'tiles': tiles})

    # - Default Events - #
    def on_tick(self):
        return

    # - Calls - #
    def update_metadata(self, **settings):
        pass

    def set_band_path(self, id, path):
        # Inform other players about change
        self.bands[id].path = path

    def create_character(
            self, name, x=0, y=0, band=None, age=0, player=False, speed=1):
        cid = uuid.uuid4()
        if player:
            self.players[cid] = player
        bid = uuid.uuid4()
        character = Character(
            cid, name, age, band, not bool(player), speed, {}, {}, {}
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
