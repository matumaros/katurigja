

import random
import string

from kivy.event import EventDispatcher

from util.threads import thread
from controllers.server import Server


class Local(EventDispatcher):
    def __init__(self, settings={}):
        # self.register_event_type('on_character_update')
        self.register_event_type('on_character_knowledge_update')
        self.register_event_type('on_tick')
        super().__init__()

        self.server = Server(settings)
        self.character = self.create_random_character(ai=False)

    @thread
    def run(self):
        self.server.run()

    def tick(self, *args):
        know = self.server.update_character_knowledge(
            self.character.id
        )
        if know:
            self.update_character_knowledge(know)
        self.dispatch('on_tick')

    def pause(self):
        self.server.pause()

    def update_character_knowledge(self, knowledge):
        pass
        # ToDo: update character knowledge and deligate related tasks

    # - Default Events - #
    def on_character_update(self):
        return

    def on_character_knowledge_update(self, know):
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
        return self.server.create_character(name=name, age=age, player=self)
