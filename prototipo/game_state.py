from player import Player
from tile_map import Tile_map
class Game_state:
    def __init__(self, playerX, playerY):
        self.__tile_map = Tile_map()
        self.__player =  Player(playerX - 60, playerY - 60, 120, 4)
        self.__objects = [self.__player] + self.__tile_map.tile_list
        self.__obstacles = self.__tile_map.tile_list
        self.__kinetic_objects = [self.__player]
        self.__command_objects = [self.__player]

    @property
    def player(self):
        return self.__player
    @property
    def objects(self):
        return self.__objects
    @property
    def kinetic_objects(self):
        return self.__kinetic_objects
    @property
    def command_objects(self):
        return self.__command_objects
    @property
    def obstacles(self):
        return self.__obstacles