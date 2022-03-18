from abc import ABC, abstractmethod
import pygame


class AbcRenderer:
    def __init__(self, screen_size):
        self._win = pygame.display.set_mode((screen_size, screen_size))
        self._screen_size = screen_size

    @abstractmethod
    def render(self):
        pass
