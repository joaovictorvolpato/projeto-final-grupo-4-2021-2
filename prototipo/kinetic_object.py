
# import pygame
# from abc import abstractmethod
# from abc_object import ABCObject
# from random import randint

# class Kinetic_obeject(ABCObject):
#     def __init__(self, initial_x: int, initial_y: int, size: int,speed:int):
#         super().__init__(initial_x, initial_y, size)
#         self.__x = initial_x
#         self.__y = initial_y
#         self.__size = size
#         self.__speed = speed
#         self.__rect = pygame.Rect(int(self.__x), int(self.__y), self.__size, self.__size)

#     @property
#     def speed(self):
#         return self.__speed

#     @abstractmethod
#     def draw(self, win):
#         pass

#     @abstractmethod
#     def change_for_camera(self):
#         pass

#     @abstractmethod
#     def update(self):
#         pass