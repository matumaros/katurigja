

import random
import string

from kivy.event import EventDispatcher
from playhouse.sqlite_ext import SqliteExtDatabase

from util.threads import thread
from controllers.server import Server


class Local(EventDispatcher):
    def __init__(self, settings={}):
        self.register_event_type('on_character_knowledge_update')

        super().__init__()

        self.server = Server(settings)
        self.db = SqliteExtDatabase('saves/serversession.save')
        self.character = self.create_random_character(ai=False)

    @thread
    def run(self):
        self.server.running = True
        while self.server.running:
            self.server.tick()
            know = self.server.update_character_knowledge(
                self.character['info']['id']
            )
            self.on_character_knowledge_update(know)

    def pause(self):
        self.server.pause()

    # - Events - #
    def on_character_knowledge_update(self, know):
        return

    # - Metadata - #
    def update_settings(self, **settings):
        self.server.update_metadata(**settings)

    # - Util - #
    def create_random_character(self, name='', age=0, ai=True):
        name = name or ''.join([
            random.choice(string.ascii_lowercase)
            for i in range(random.randint(2, 15))
        ]).title()
        age = age or random.randint(16, 60)
        return self.server.create_character(name, age, ai)
