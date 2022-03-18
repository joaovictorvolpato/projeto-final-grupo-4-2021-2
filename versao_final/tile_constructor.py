from abc_constructor import Constructor
from tile import Tile
from medkit import Medkit


class TileConstructor(Constructor):
    def __init__(self, level):
        super().__init__(['x', 'm'], ['object'], level)
        self._level = level

    def instantiate(self, x, y, tag):
        self.__init__(self._level)
        SIZE = self._config.get('tile-size')
        if tag == 'x':
            wall = Tile(x*SIZE, y*SIZE, SIZE,
                        f'sprites/lv{self._level}_tiles/x.png')
            self._lists.append('obstacle')
            return wall

        if tag == 'm':
            medkit = Medkit(x*SIZE, y*SIZE, SIZE,
                            f'sprites/m.png')
            self._lists.append('interactable')
            return medkit
