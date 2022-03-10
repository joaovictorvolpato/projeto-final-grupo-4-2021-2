from tile import Tile
from key import Key


class Tile_map:
    def __init__(self, tilemap, tile_size):
        self.__tile_size = tile_size
        self.__tilemap = tilemap
        self.__tile_list = []
        self.__obstacle_list = []
        self.__event_list = []
        self.fill_lists()

    @property
    def tile_list(self):
        return self.__tile_list

    @property
    def obstacle_list(self):
        return self.__obstacle_list

    @property
    def event_list(self):
        return self.__event_list

    def fill_lists(self):
        for y, row in enumerate(self.__tilemap):
            for x, tile in enumerate(row):
                if tile == 'x':
                    SIZE = self.__tile_size
                    wall = Tile(x*SIZE, y*SIZE, SIZE, (255, 0, 0))
                    self.__tile_list.append(wall)
                    self.__obstacle_list.append(wall)
                elif tile == 'o':
                    SIZE = self.__tile_size
                    wall = Tile(x*SIZE, y*SIZE, SIZE, (0, 255, 0))
                    self.__tile_list.append(wall)
                elif tile == '1' or tile == '2':
                    SIZE = self.__tile_size
                    key = Key(x*SIZE, y*SIZE, SIZE, int(tile))
                    self.__tile_list.append(key)
                    self.__event_list.append(key)
