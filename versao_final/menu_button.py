import pygame


class MenuButton:
    def __init__(
            self,
            img: str,
            destination: str,
            x: int,
            y: int):
        self._img = pygame.image.load(img)
        self._destination = destination
        self._rect = self._img.get_rect()
        self._rect.topleft = (x, y)

    @property
    def img(self):
        return self._img

    @property
    def destination(self):
        return self._destination

    @property
    def rect(self):
        return self._rect
