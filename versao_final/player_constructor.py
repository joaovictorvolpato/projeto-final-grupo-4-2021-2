from abc_constructor import Constructor
from player import Player


class PlayerConstructor(Constructor):
    def __init__(self, level):
        super().__init__(['p'], [
            'object', 'kinetic', 'command'], level)

    def instantiate(self, x, y, tag):
        SIZE = self._config.get('tile-size')
        PLAYER_SPEED = self._config.get('player-speed')
        player = Player(x*SIZE, y*SIZE, SIZE, PLAYER_SPEED)
        return player
