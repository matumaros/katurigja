

from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from views.world import World


class Game(Screen):
    Builder.load_file('views/game.kv')

    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.set_player(client.character)

        self.client.bind(
            on_tick=lambda wg, band=self.character.band:
                self.update_world_center(band.pos)
        )
        self.client.bind(
            on_band_update=lambda ev, band: self.world.update_band(band)
        )
        self.client.bind(
            on_character_knowledge_update=self.update_character_knowledge
        )
        self.client.bind(
            on_character=self.set_player
        )
        self.world.bind(
            on_touch_down=lambda wg, ev: self.on_action(ev)
        )

    def on_enter(self):
        self.client.run()

    def set_player(self, player):
        self.character = player

    def on_action(self, ev):
        if ev.is_mouse_scrolling:
            return
        pos = ev.pos
        off_x = (pos[0] - self.world.center[0]) / self.world.zoom
        off_y = (pos[1] - self.world.center[1]) / self.world.zoom
        cx, cy = self.world.real_center[0], self.world.real_center[1]
        path = [(cx + off_x, cy + off_y)]

        self.client.set_band_path(path)

    def move_player_to(self, x, y):
        self.client.move_player_to(x, y)

    def update_world_center(self, pos):
        self.world.real_center = pos

    def update_character_knowledge(self, ev, knowledge):
        self.world.update_tiles(knowledge['tiles'])
