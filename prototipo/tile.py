from abc import ABC
from tempDB import *
import pygame
import copy
from abc_object import ABCObject
class Tile(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        super().__init__(initial_x, initial_y, size)
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__color = (21,10, 150)
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)
        # self.__offset = pygame.Vector2()

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

    def draw(self, win, offset):
        fake_rect = copy.deepcopy(self.__rect)
        fake_rect.topleft -= offset
        pygame.draw.rect(win, self.__color, fake_rect)