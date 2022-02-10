from player import Player
from command_object import Command_object
from kinetic_object import Kinetic_obeject

class Game_state:
    def __init__(self, playerX, playerY):
        self.__player =  Player(playerX, playerY, 50, (255, 3, 10), 4, {'up': False, 'down': False, 'right': False, 'left': False})
        self.__inimigo =  Kinetic_obeject(playerX, playerY, 50, (0, 0, 0), 4)
        self.__objects = [self.__player, self.__inimigo]
        self.__kinetic_objects = [self.__player, self.__inimigo]
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