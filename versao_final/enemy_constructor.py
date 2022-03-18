from abc_constructor import Constructor
from simple_enemy import SimpleEnemy
from smart_enemy import SmartEnemy
from freez_enemy import FreezEnemy


class EnemyConstructor(Constructor):
    def __init__(self, level):
        super().__init__(['e', 's', 'f'], ['object', 'interactable'], level)

    def instantiate(self, x, y, tag):
        self.__init__(self._level)
        SIZE = self._config.get('tile-size')
        SPEED = self._config.get('enemy-speed')
        SPEED_SMART = self._config.get('smart-enemy-speed')
        if tag == 'e':
            simple_enemy = SimpleEnemy(
                x*SIZE, y*SIZE, SIZE, SPEED, f'sprites/lv{self._level}_tiles/e.png')
            self._lists.append('kinetic')
            return simple_enemy
        if tag == 's':
            smart_enemy = SmartEnemy(
                x*SIZE, y*SIZE, SIZE, SPEED_SMART, f'sprites/lv{self._level}_tiles/s.png')
            self._lists.append('kinetic')
            self._lists.append('request')
            return smart_enemy
        if tag == 'f':
            freez_enemy = FreezEnemy(
                x*SIZE, y*SIZE, SIZE, f'sprites/lv{self._level}_tiles/f.png')
            return freez_enemy
