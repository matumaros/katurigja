

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from controllers.server import Server
from controllers.world import World


class Game(FloatLayout):
    Builder.load_file('views/game.kv')

    def __init__(self, server=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not server:
            self.server = Server()
        else:
            self.server = server
        self.player = self.server.create_ruler(name='Matumaros', age=23)

    def move_character(self, event):
        self.server.update_character(self.player)
