import pygame
from abc import ABC


class ABCObject(ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int, sprite: str):
        self._size = size
        self._sprite = pygame.image.load(sprite)
        self._sprite = pygame.transform.scale(
            self._sprite, (self._size, self._size))
        self._rect = self._sprite.get_rect()
        self._rect.topleft = (initial_x, initial_y)

    @property
    def size(self):
        return self._size

    @property
    def rect(self):
        return self._rect

    @property
    def sprite(self):
        return self._sprite

    def change_sprite(self, path):
        self._sprite = pygame.image.load(path)
        self._sprite = pygame.transform.scale(
            self._sprite, (self._size, self._size))

    @size.setter
    def size(self, new_size: int):
        if isinstance(new_size, int):
            self._size = new_size
