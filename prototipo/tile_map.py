from tile import Tile
class Tile_map:
    def __init__(self, tilemap, tile_size):
        self.__tile_size = tile_size
        self.__tilemap = tilemap
        self.__tile_list = []
        self.fill_tile_list()

    @property
    def tile_list(self):
        return self.__tile_list
        
    def fill_tile_list(self):
        for y, row in enumerate(self.__tilemap):
            for x, tile in enumerate(row):
                if tile == 'x':
                    SIZE = self.__tile_size
                    wall = Tile(x*SIZE, y*SIZE, SIZE)
                    self.__tile_list.append(wall)

