

from models.character import Character


class Server:
    def get_tile(self, x, y):
        return {
            'altitude': 0,
            'grass': 1.0,
            'rock': 0.0,
        }

    def create_ruler(self, name, age=0, ai=False):
        character = Character(name, age, ai)
        return character

    def update_character(self, character):
        pass
