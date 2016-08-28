#!/usr/bin/env python


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Game(App):
    view = BoxLayout()

    def build(self):
        return self.view


if __name__ == '__main__':
    from controllers.world import World

    game = Game()
    game.view.add_widget(World())
    game.run()
