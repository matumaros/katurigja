

from math import sqrt
import random
import string

from kivy.event import EventDispatcher

from util.threads import thread
from controllers.server import Server


class Local(EventDispatcher):
    def __init__(self, settings={}):
        self.register_event_type('on_character_update')
        self.register_event_type('on_character_knowledge_update')
        super().__init__()

        self.server = Server(settings)
        self.character = self.create_random_character(ai=False)

        self.server.bind(on_tick=self.on_tick)

    @thread
    def run(self):
        self.server.run()

    def on_tick(self, *args):
        self.update_character()
        know = self.server.update_character_knowledge(
            self.character.id
        )
        self.update_character_knowledge(know)

    def pause(self):
        self.server.pause()

    def update_character(self):
        if self.character.path:
            goal = self.character.path[0]
            x, y = self.character.x, self.character.y
            a = abs(x - goal[0])**2
            b = abs(y - goal[1])**2
            distance = sqrt(a + b)
            factor = self.character.speed / distance
            dx, dy = goal[0] * factor, goal[1] * factor
            self.character.x += dx
            self.character.y += dy

            self.server.update_character(self.character)
        self.dispatch('on_character_update')

    def update_character_knowledge(self, know):
        self.dispatch('on_character_knowledge_update', know)

    # - Default Events - #
    def on_character_update(self):
        return

    def on_character_knowledge_update(self, know):
        return

    # - Metadata - #
    def update_settings(self, **settings):
        self.server.update_metadata(**settings)

    def set_player_path(self, path):
        self.character.path = path
        self.server.set_character_path(self.character.id, path)

    # - Util - #
    def create_random_character(self, name='', age=0, ai=True):
        name = name or ''.join([
            random.choice(string.ascii_lowercase)
            for i in range(random.randint(2, 15))
        ]).title()
        age = age or random.randint(16, 60)
        return self.server.create_character(name=name, age=age, ai=ai)
