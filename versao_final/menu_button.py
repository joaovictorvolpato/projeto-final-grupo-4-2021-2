import pygame


class MenuButton:
    def __init__(self, img: str, destination: str, x: int, y: int):
        self._img = pygame.image.load(img)
        DEFAULT_SIZE = (100, 50)
        self._img = pygame.transform.scale(self._img, DEFAULT_SIZE)
        self._destination = destination
        self._rect = self._img.get_rect()
        self._rect.topleft = (x, y)

    @property
    def img(self):
        return self._img

    @property
    def destination(self):
        return self._destination

    # @property
    # def x(self):
    #     return self._x

    # @property
    # def y(self):
    #     return self._y

    @property
    def rect(self):
        return self._rect
