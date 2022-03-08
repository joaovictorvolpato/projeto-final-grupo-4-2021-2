import pygame
import copy
from abc_object import ABCObject


class Tile(ABCObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, color):
        super().__init__(initial_x, initial_y, size, color)
