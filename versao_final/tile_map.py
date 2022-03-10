from level_dao import Level_dao
from tile import Tile
from key import Key
from level_dao import Level_dao
from player import Player
from simple_enemy import Simple_enemy
from smart_enemy import Smart_enemy


class Tile_map_constructor:
    def __init__(self, level):
        self.__level_dao = Level_dao('levels.json', level)
        self.__tile_size = self.__level_dao.get('tilesize')
        self.__tilemap = self.__level_dao.get('tilemap')
        self.__player = None
        self.__object_list = []
        self.__obstacle_list = []
        self.__event_list = []
        self.__enemy_list = []
        self.__command_list = []
        self.__kinetic_list = []
        self.fill_init()

    @property
    def kinetic_list(self):
        return self.__kinetic_list

    @property
    def command_list(self):
        return self.__command_list

    @property
    def enemy_list(self):
        return self.__enemy_list

    @property
    def player(self):
        return self.__player

    @property
    def object_list(self):
        return self.__object_list

    @property
    def obstacle_list(self):
        return self.__obstacle_list

    @property
    def event_list(self):
        return self.__event_list

    def fill_init(self):
        for y, row in enumerate(self.__tilemap):
            for x, tile in enumerate(row):

                # mudar para classes dps, tirar ifs

                if tile == 'x':
                    SIZE = self.__tile_size
                    wall = Tile(x*SIZE, y*SIZE, SIZE, (255, 0, 0))
                    self.__object_list.append(wall)
                    self.__obstacle_list.append(wall)
                elif tile == 'o':
                    SIZE = self.__tile_size
                    wall = Tile(x*SIZE, y*SIZE, SIZE, (0, 255, 0))
                    self.__object_list.append(wall)
                elif isinstance(tile, int):
                    SIZE = self.__tile_size
                    key = Key(x*SIZE, y*SIZE, SIZE, int(tile))
                    self.__object_list.append(key)
                    self.__event_list.append(key)
                elif tile == 'p' and self.__player is None:
                    SIZE = self.__tile_size
                    PLAYERSPEED = self.__level_dao.get("player_speed")
                    self.__player = Player(x*SIZE, y*SIZE,
                                           SIZE, PLAYERSPEED)
                    self.__object_list.append(self.__player)
                    self.__kinetic_list.append(self.__player)
                    self.__command_list.append(self.__player)
                elif tile == 'e':
                    SIZE = self.__tile_size
                    ENEMYSPEED = self.__level_dao.get('enemy_speed')
                    enemy = Simple_enemy(x*SIZE, y*SIZE,
                                         SIZE, ENEMYSPEED)
                    self.__enemy_list.append(enemy)
                    self.__kinetic_list.append(enemy)
                    self.__object_list.append(enemy)
                elif tile == 's':
                    SIZE = self.__tile_size
                    ENEMYSPEED = self.__level_dao.get('smart_speed')
                    enemy = Smart_enemy(x*SIZE, y*SIZE,
                                         SIZE, ENEMYSPEED, self.player)
                    self.__enemy_list.append(enemy)
                    self.__kinetic_list.append(enemy)
                    self.__object_list.append(enemy)
