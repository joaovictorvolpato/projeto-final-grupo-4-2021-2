from abc import abstractmethod
import pygame
from abc_object import ABCObject

class Command_object(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        super().__init__(initial_x, initial_y, size)
        self.__commands = {}
    
    @property
    def commands(self):
        return self.__commands
    
    @abstractmethod
    def execute_commands(self):
        pass