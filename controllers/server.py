

from playhouse.sqlite_ext import SqliteExtDatabase

from util.threads import thread
from models.character import Character


class Server:
    def __init__(self, settings={}):
        self.db = SqliteExtDatabase('saves/serversession.save')

        with open('maps/index', 'r') as f:
            maps = yaml.load(f.read())
        module = import_module(map_name)
        gmap = maps[map_name]
        self._map = getattr(module, gmap)
        running = False

        self.update_metadata(**settings)
        self.host()

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
        running = False

    # - Metadata - #
    def update_metadata(**settings):
        pass

    # - Data - #
    def create_character(self, name, age=0, x=0, y=0, ai=True):
        character = Character(db=self.db, name, age, x, y, ai)
        character.save()
        return character

    def update_character_knowledge(self, character_id):
        return  #knowledge
