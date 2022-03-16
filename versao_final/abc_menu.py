from abc import ABC, abstractmethod
import pygame
import sys


class AbcMenu(ABC):
    def __init__(self, screen_size: int, buttons: dict):
        self._win = pygame.display.set_mode((screen_size, screen_size))
        self._buttons = buttons
        self._clk = pygame.time.Clock()

    def _draw_text(self, text, color, x, y):
        textobj = self._font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        self._win.blit(textobj, textrect)

    @abstractmethod
    def execute_menu_routine(self):
        pass

    def menu_loop(self):
        while True:

            self.execute_menu_routine()

            pygame.display.flip()
            self._clk.tick(60)
