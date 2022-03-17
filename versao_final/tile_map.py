from level_dao import Level_dao
from player_constructor import Player_constructor
from tile_constructor import Tile_constructor
from enemy_constructor import Enemy_constructor
from event_constructor import Event_constructor


class TileMapConstructor:
    def __init__(self, level):
        self.__level_dao = Level_dao(level)
        self.__tilemap = self.__level_dao.get('tile-map')
        self.__object_list = []
        self.__obstacle_list = []
        self.__event_list = []
        self.__interactable_list = []
        self.__command_list = []
        self.__kinetic_list = []
        self.__request_list = []
        self.__lists_dict = {'object': self.__object_list,
                             'obstacle': self.__obstacle_list,
                             'event': self.__event_list,
                             'interactable': self.__interactable_list,
                             'command': self.__command_list,
                             'kinetic': self.__kinetic_list,
                             'request': self.__request_list}
        self.__constructors = [Player_constructor(), Tile_constructor(),
                               Enemy_constructor(), Event_constructor()]
        self.fill_init()
        # mudar caso dois players depois
        self.__player = self.__command_list[0]

    @property
    def kinetic_list(self):
        return self.__kinetic_list

    @property
    def command_list(self):
        return self.__command_list

    @property
    def interactable_list(self):
        return self.__interactable_list

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

    @property
    def request_list(self):
        return self.__request_list

    def fill_init(self):
        for y, row in enumerate(self.__tilemap):
            for x, tile in enumerate(row):
                for constructor in self.__constructors:
                    for tag in constructor.tags:
                        if tile == tag:
                            obj = constructor.instantiate(x, y, tag)
                            for list in constructor.lists:
                                self.__lists_dict[list].append(obj)
                # mudar para classes dps, tirar ifs

                # if tile == 'x':
                #     SIZE = self.__tile_size
                #     wall = Tile(x*SIZE, y*SIZE, SIZE, (255, 0, 0))
                #     self.__object_list.append(wall)
                #     self.__obstacle_list.append(wall)
                # elif tile == 'o':
                #     SIZE = self.__tile_size
                #     wall = Tile(x*SIZE, y*SIZE, SIZE, (0, 255, 0))
                #     self.__object_list.append(wall)
                # elif isinstance(tile, int):
                #     SIZE = self.__tile_size
                #     key = Key(x*SIZE, y*SIZE, SIZE, int(tile))
                #     self.__object_list.append(key)
                #     self.__event_list.append(key)
                # elif tile == 'p' and self.__player is None:
                #     SIZE = self.__tile_size
                #     PLAYERSPEED = self.__level_dao.get("player_speed")
                #     self.__player = Player(x*SIZE, y*SIZE,
                #                            SIZE, PLAYERSPEED)
                #     self.__object_list.append(self.__player)
                #     self.__kinetic_list.append(self.__player)
                #     self.__command_list.append(self.__player)
                # elif tile == 'e':
                #     SIZE = self.__tile_size
                #     ENEMYSPEED = self.__level_dao.get('enemy_speed')
                #     enemy = Simple_enemy(x*SIZE, y*SIZE,
                #                          SIZE, ENEMYSPEED)
                #     self.__enemy_list.append(enemy)
                #     self.__kinetic_list.append(enemy)
                #     self.__object_list.append(enemy)
