from player import Player
from enemy import Enemy
from tile_map import Tile_map
class Game_state:
    def __init__(self, playerX, playerY):
        self.__tile_map = Tile_map()
        self.__player =  Player(playerX - 60, playerY - 60, 120, 4)
        enemy1 = Enemy(playerX, playerX, 150, 4, 5)
        self.__objects = [self.__player, enemy1] + self.__tile_map.tile_list
        self.__obstacles = self.__tile_map.tile_list
        self.__enemys = [enemy1]
        self.__kinetic_objects = [self.__player, enemy1]
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
    @property
    def enemys(self):
        return self.__enemys