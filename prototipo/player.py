from calendar import c
import pygame, sys
import math
from abc_object import ABCObject

class Player(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple, speed:int, commands:dict ):
        super().__init__(initial_x, initial_y, size,  color)
        #sprites
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__color = color
        self.__speed = speed
        self.__commands = commands
        self.__velX = 0
        self.__velY = 0

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands

    # usar para normalizar os vetores de velocidade, caso contrario, anda mais rápido nas diagonais
    def normalize(self):
        if self.__velX != 0 and self.__velY != 0:
            self.__velX *=  1/math.sqrt(2)
            self.__velY *= 1/math.sqrt(2)

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)

    def execute_commands(self):
        self.__velX = 0
        self.__velY = 0
        if self.__commands['left'] and not self.__commands['right']:
            self.__velX = -self.__speed
        if self.__commands['right'] and not self.__commands['left']:
            self.__velX = self.__speed
        if self.__commands['up'] and not self.__commands['down']:
            self.__velY = -self.__speed
        if self.__commands['down'] and not self.__commands['up']:
            self.__velY = self.__speed
        
        self.normalize()
        self.__x += self.__velX
        self.__y += self.__velY

    def chance_for_camera():
        pass

    def update(self):
        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)

    


