#!/usr/bin/env python


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Katurigja(App):
    view = BoxLayout()

    def build(self):
        return self.view


if __name__ == '__main__':
    from views.menu import Menu

    game = Katurigja()
    game.view.add_widget(Menu())
    game.run()
