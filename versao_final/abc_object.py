import pygame
from abc import ABC, abstractmethod
import copy


class ABCObject(ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int, color: tuple):
        self._size = size
        self._rect = pygame.Rect(
            initial_x, initial_y, self._size, self._size)
        self._color = color

    @property
    def size(self):
        return self._size

    @property
    def rect(self):
        return self._rect

    @property
    def color(self):
        return self._color

    @size.setter
    def size(self, new_size: int):
        if isinstance(new_size, int):
            self._size = new_size

    @color.setter
    def color(self, new_color: tuple):
        if isinstance(new_color, tuple):
            if len(new_color) == 3 and isinstance(new_color[1], int) and isinstance(new_color[0], int) and isinstance(new_color[2], int):
                self._color = new_color
