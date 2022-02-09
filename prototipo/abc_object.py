import pygame
from abc import ABC

class Obeject(ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple):
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__color = color
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)

    
