from tempDB import *
import pygame
class Tile:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__size = SIZE
        self.__color = (21,10, 150)
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    def change_for_camera(self, vel_x, vel_y):
        self.__x -= vel_x
        self.__y -= vel_y

    def update(self):
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)
    