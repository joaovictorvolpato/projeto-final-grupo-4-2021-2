import pygame
from abc_object import ABCObject

class Command_object(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple, commands: dict):
        super().__init__(initial_x, initial_y, size, color)
        self.__commands = commands
        
    
    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands

    def update():
        pass

    def change_for_camera():
        pass

    def draw(self, win):
        pass

    def execute_commands(self):
        pass
