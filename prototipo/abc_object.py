import pygame
from abc import ABC, abstractmethod

class ABCObject(ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def size(self):
        return self.__size

    @property
    def rect(self):
        return self.__rect


    @abstractmethod
    def draw(self, win):
        pass


    
