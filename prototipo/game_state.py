from player import Player
from level_dao import Level_dao
from tile_map import Tile_map
class Game_state:
    def __init__(self, playerX, playerY):
        self.level_dao = Level_dao('prototipo/levels.json', 1)
        self.__tile_map = Tile_map(self.level_dao.get("tilemap"))
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