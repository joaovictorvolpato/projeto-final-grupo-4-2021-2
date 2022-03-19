from abc import ABC
import pygame


class AbcMenu(ABC):
    def __init__(self, buttons: list, background: str, name: str):
        self._buttons = buttons
        self._bg = pygame.image.load(background)
        self._name = name

    @property
    def buttons(self):
        return self._buttons

    @property
    def bg(self):
        return self._bg

    @property
    def name(self):
        return self._name
