#!/usr/bin/env python


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition


class Katurigja(App):
    view = ScreenManager(transition=FadeTransition())

    def build(self):
        return self.view


if __name__ == '__main__':
    from controllers.client import Local
    from views.menu import Menu
    from views.game_setup import GameSetup
    from views.game import Game

    game = Katurigja()
    client = Local()

    game.view.add_widget(
        Menu(
            name='main_menu',
        )
    )
    game.view.add_widget(
        GameSetup(
            last_screen='main_menu',
            client=client,
            name='game_setup',
        )
    )
    game.view.add_widget(
        Game(
            client=client,
            name='game',
        )
    )
    game.run()
