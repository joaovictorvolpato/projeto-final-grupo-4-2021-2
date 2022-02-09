import pygame
from abc_object import Object

class Static_object(Object):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple, command: dict):
        Static_object.__init__(self)
        self.__commands = command

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands

    def execute_commands(self):
        pass


    


