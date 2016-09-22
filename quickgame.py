

from main import Katurigja
from views.game import Game
from controllers.client import Local


game = Katurigja()
client = Local({
    'map_name': 'flat_grassland'
})
game.bind(on_stop=lambda *args, **kwargs: client.pause())

game.view.add_widget(Game(client))
game.run()
