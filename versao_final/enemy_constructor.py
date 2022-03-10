from abc_constructor import Constructor
from simple_enemy import Simple_enemy


class Enemy_constructor(Constructor):
    def __init__(self):
        super().__init__(['e'], ['object', 'interactable'])

    def instantiate(self, x, y, tag):
        self.__init__()
        SIZE = self._config.get('tile-size')
        SPEED = self._config.get('enemy-speed')
        if tag == 'e':
            simple_enemy = Simple_enemy(
                x*SIZE, y*SIZE, SIZE, SPEED)
            self._lists.append('kinetic')
            return simple_enemy
