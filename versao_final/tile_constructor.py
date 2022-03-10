from abc_constructor import Constructor
from tile import Tile


class Tile_constructor(Constructor):
    def __init__(self):
        super().__init__(['x', 'g'], ['object'])

    def instantiate(self, x, y, tag):
        self.__init__()
        SIZE = self._config.get('tile-size')
        if tag == 'x':
            wall = Tile(x*SIZE, y*SIZE, SIZE, (255, 0, 0))
            self._lists.append('obstacle')
            return wall
        elif tag == 'g':
            grass = Tile(x*SIZE, y*SIZE, SIZE, (0, 255, 0))
            return grass
