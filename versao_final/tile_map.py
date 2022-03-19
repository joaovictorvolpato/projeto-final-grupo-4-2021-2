from level_dao import LevelDao
from player_constructor import PlayerConstructor
from tile_constructor import TileConstructor
from enemy_constructor import EnemyConstructor
from event_constructor import EventConstructor
from background_obj import Background


class TileMapConstructor:
    def __init__(self, level):
        self.__level_dao = LevelDao(level)
        self.__tilemap = self.__level_dao.get('tile-map')
        self.__object_list = [self.__get_back_ground(level)]
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
        self.__constructors = [PlayerConstructor(level), TileConstructor(level),
                               EnemyConstructor(level), EventConstructor(level)]
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

    def __get_back_ground(self, level):
        size_y = len(self.__tilemap)
        size_x = len(self.__tilemap[0])
        return Background(size_x, size_y, f'sprites/lv{level}_tiles/background.png')

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
