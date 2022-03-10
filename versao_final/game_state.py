from abc_singleton import Singleton
from tile_map import Tile_map_constructor


class Game_state(metaclass=Singleton):
    def __init__(self, level):
        self.__tile_map = Tile_map_constructor(level)
        self.__obstacles = self.__tile_map.obstacle_list
        self.__player = self.__tile_map.player
        self.__interactables = self.__tile_map.interactable_list
        self.__objects = self.__tile_map.object_list
        self.__kinetic_objects = self.__tile_map.kinetic_list
        self.__command_objects = self.__tile_map.command_list
        self.__event_objects = self.__tile_map.event_list

    def change_level(self, next_level: int):
        self.__init__(next_level)

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
    def event_objects(self):
        return self.__event_objects

    @property
    def interactable(self):
        return self.__interactables
