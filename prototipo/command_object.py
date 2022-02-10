import pygame
from static_object import Static_object

class Command_object(Static_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple, commands: dict, speed:int):
        Command_object.__init__(self)
        self.__speed = speed
        self.__x = initial_x
        self.__y = initial_y
        self.__color = color
        self.__size = size
        self.__rect = pygame.Rect(self.__x, self.__y, self.__size, self.__size)
    
    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands

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

    def update(self):
        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)