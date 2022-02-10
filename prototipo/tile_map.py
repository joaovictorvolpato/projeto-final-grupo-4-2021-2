from tempDB import *
from tile import Tile
class Tile_map:
    def __init__(self):
        self.__tilemap = MAP1
        self.__tile_list = []
        self.fill_tile_list()

    @property
    def tile_list(self):
        return self.__tile_list
        
    def fill_tile_list(self):
        for y, row in enumerate(self.__tilemap):
            for x, tile in enumerate(row):
                if tile == 'x':
                    wall = Tile(x*SIZE, y*SIZE)
                    self.__tile_list.append(wall)

