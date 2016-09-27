

import random
import string

from kivy.event import EventDispatcher

from controllers.server import Server
from controllers.band import Band


class Local(EventDispatcher):
    def __init__(self, settings={}):
        self.register_event_type('on_band_update')
        self.register_event_type('on_character_knowledge_update')
        self.register_event_type('on_tick')
        super().__init__()

        self.server = Server(settings)
        self.server.local_client = self
        self.bands = {}
        self.character = self.create_random_character(ai=False)
        self.bands[self.character.band.id] = Band(model=self.character.band)

    def run(self):
        self.server.run()

    def tick(self, first=False):
        for band_id, band in self.bands.items():
            model = band.model
            if first or model.path:
                self.dispatch('on_band_update', model)
        self.dispatch('on_tick')

    def pause(self):
        self.server.pause()

    def update_character_knowledge(self, knowledge):
        self.dispatch('on_character_knowledge_update', knowledge)

    # - Default Events - #
    def on_band_update(self, band_model):
        return

    def on_character_knowledge_update(self, knowledge):
        return

    def on_tick(self, *args):
        return

    # - Metadata - #
    def update_settings(self, **settings):
        self.server.update_metadata(**settings)

    def set_band_path(self, path):
        if self.character.id == self.character.band.leader.id:
            self.character.band.path = path
            self.server.set_band_path(self.character.band.id, path)

    # - Util - #
    def create_random_character(self, name='', age=0, ai=True):
        name = name or ''.join([
            random.choice(string.ascii_lowercase)
            for i in range(random.randint(2, 15))
        ]).title()
        age = age or random.randint(16, 60)
        return self.server.create_character(
            name=name, age=age, player=self, speed=0.1  # TESTING
        )
