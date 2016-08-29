

from playhouse.sqlite_ext import SqliteExtDatabase

from models.character import Character


class Server:
    def __init__(self):
        self.db = SqliteExtDatabase('saves/serversession.save')

    def get_tile(self, x, y):
        return {
            'altitude': 0,
            'grass': 1.0,
            'rock': 0.0,
        }

    def create_ruler(self, name, age=0, ai=False):
        character = Character(db=self.db, name, age, ai)
        character.save()
        return character

    def update_character(self, character):
        pass
