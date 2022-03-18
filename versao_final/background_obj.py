import pygame
from config_dao import ConfigDao


class Background:
    def __init__(self, sizeX: int, sizeY: int, sprite: str):
        self._dao = ConfigDao()
        SIZE = self._dao.get('tile-size')
        self._size = (sizeX * SIZE, sizeY * SIZE)
        self._sprite = pygame.image.load(sprite)
        self._sprite = pygame.transform.scale(
            self._sprite, (self._size[0], self._size[1]))
        self._rect = self._sprite.get_rect()
        self._rect.topleft = (0, 0)

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
