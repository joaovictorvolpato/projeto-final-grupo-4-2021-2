from abc_singleton import Singleton
from tile_map import TileMapConstructor
from player import Player
import pygame


class GameState(metaclass=Singleton):
    def __init__(self, level):
        self.__bg = pygame.image.load(
            f'sprites/lv{level}_tiles/background.png')
        self.__tile_map = TileMapConstructor(level)
        self.__obstacles = self.__tile_map.obstacle_list
        self.__player = self.__tile_map.player
        self.__interactables = self.__tile_map.interactable_list
        self.__objects = self.__tile_map.object_list
        self.__kinetic_objects = self.__tile_map.kinetic_list
        self.__command_objects = self.__tile_map.command_list
        self.__event_objects = self.__tile_map.event_list
        self.__request_objects = self.__tile_map.request_list
        self.__next_state = None

    def change_level(self, next_level: int):
        self.__init__(next_level)

    @property
    def player(self):
        return self.__player

    @property
    def next_state(self):
        return self.__next_state

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
    def interactables(self):
        return self.__interactables

    @property
    def request_objects(self):
        return self.__request_objects

    @property
    def bg(self):
        return self.__bg

    @player.setter
    def player(self, new):
        if isinstance(new, Player):
            self.__player = new
            return
        print('não é um player')

    @next_state.setter
    def next_state(self, new_state):
        self.__next_state = new_state
