

from main import Katurigja
from controllers.game import Game
from controllers.client import Local


game = Katurigja()
client = Local({
    'map_name': 'flat_grassland'
})

game.view.add_widget(Game(client))
game.run()
