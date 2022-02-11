from abc import abstractmethod
import pygame
from abc_object import ABCObject

class Command_object(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int,commands: dict):
        super().__init__(initial_x, initial_y, size)
        self.__commands = commands
        
    
    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands

    @abstractmethod
    def update():
        pass
    
    @abstractmethod
    def change_for_camera():
        pass

    @abstractmethod
    def draw(self, win):
        pass

    @abstractmethod
    def execute_commands(self):
        pass