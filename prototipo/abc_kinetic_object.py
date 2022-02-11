import pygame
from abc import ABC , abstractmethod
from abc_object import ABCObject

class Kinetic_object(ABCObject, ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int,speed:int):
        super().__init__(initial_x, initial_y, size)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @abstractmethod
    def check_collisions(self, obstacles: list):
        pass

    @abstractmethod
    def update(self):
        pass
