import pygame
from abc import ABC, abstractmethod

class ABCObject(ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        self.__size = size
        self.__rect = pygame.Rect(initial_x, initial_y, self.__size, self.__size)

    @property
    def size(self):
        return self.__size

    @property
    def rect(self):
        return self.__rect


    @abstractmethod
    def draw(self, win):
        pass


    
