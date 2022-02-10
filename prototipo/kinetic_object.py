from ast import While
import pygame
from abc_object import ABCObject
from random import randint

class Kinetic_obeject(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, color:tuple, speed:int):
        super().__init__(initial_x, initial_y, size, color)
        self.__x = initial_x
        self.__y = initial_y
        self.__size = size
        self.__speed = speed
        self.__color = color
        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)

    @property
    def speed(self):
        return self.__speed

    def draw(self, win):
        pygame.draw.rect(win, self.__color, self.__rect)


    def change_for_camera(self):
        pass

    def update(self):
        speed_x = 0
        speed_y = 0
        direction = 0

        if self.__x <= 20 or self.__y >= 580:
            direction *= -1
            speed_x = randint(0, 8) * direction
            speed_y = randint(0, 8) * direction
 
        
        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction
 

        if self.__x <= 20 or self.__y >= 580:
            direction *= -1
            speed_x = randint(0, 8) * direction
            speed_y = randint(0, 8) * direction
 
        
        if speed_x == 0 and speed_y == 0:
            speed_x = randint(2, 8) * direction
            speed_y = randint(2, 8) * direction
 
        self.__x += speed_x
        self.__y += speed_y

        self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)