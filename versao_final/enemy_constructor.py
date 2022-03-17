from abc_constructor import Constructor
from simple_enemy import Simple_enemy
from smart_enemy import Smart_enemy


class Enemy_constructor(Constructor):
    def __init__(self):
        super().__init__(['e', 's'], ['object', 'interactable'])

    def instantiate(self, x, y, tag):
        self.__init__()
        SIZE = self._config.get('tile-size')
        SPEED = self._config.get('enemy-speed')
        SPEED_SMART = self._config.get('smart-enemy-speed')
        if tag == 'e':
            simple_enemy = Simple_enemy(
                x*SIZE, y*SIZE, SIZE, SPEED)
            self._lists.append('kinetic')
            self._lists.append('request')
            return simple_enemy
        if tag == 's':
            smart_enemy = Smart_enemy(
                x*SIZE, y*SIZE, SIZE, SPEED_SMART)
            self._lists.append('kinetic')
            self._lists.append('request')
            return smart_enemy
