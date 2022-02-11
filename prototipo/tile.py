from tempDB import *
import pygame
class Tile:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__size = SIZE
        self.__color = (21,10, 150)
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    @property
    def rect(self):
        return self.__rect

    @property
    def size(self):
        return self.__size

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @property
    def color(self):
        return self.__color

    def update(self):
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    # def draw(self, win):
    #     pygame.draw.rect(win, self.__color, self.__rect)
    