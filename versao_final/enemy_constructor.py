from abc_constructor import Constructor
from simple_enemy import SimpleEnemy
from smart_enemy import SmartEnemy


class EnemyConstructor(Constructor):
    def __init__(self):
        super().__init__(['e', 's'], ['object', 'interactable'])

    def instantiate(self, x, y, tag):
        self.__init__()
        SIZE = self._config.get('tile-size')
        SPEED = self._config.get('enemy-speed')
        SPEED_SMART = self._config.get('smart-enemy-speed')
        if tag == 'e':
            simple_enemy = SimpleEnemy(
                x*SIZE, y*SIZE, SIZE, SPEED)
            self._lists.append('kinetic')
            self._lists.append('request')
            return simple_enemy
        if tag == 's':
            smart_enemy = SmartEnemy(
                x*SIZE, y*SIZE, SIZE, SPEED_SMART)
            self._lists.append('kinetic')
            self._lists.append('request')
            return smart_enemy
