import pygame


class MenuButton:
    def __init__(self, img: str, destination: str, x: int, y: int):
        self._img = pygame.image.load(img)
        self._destination = destination
        self._x = x
        self._y = y

    @property
    def img(self):
        return self._img

    @property
    def destination(self):
        return self._destination

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
