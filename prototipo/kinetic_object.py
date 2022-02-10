import pygame
from static_object import Static_object

class Kinetic_obeject(Static_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple, speed:int):
        super.__init__(self)
        self.__speed = speed
        self.__x = initial_x
        self.__y = initial_y
        self.__color = color
        self.__size = size
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)

    def move(self):
        #logica de movimento dos inimigos
        self.__x += self.__speed
        self.__y += self.__speed

    def update(self):
        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)