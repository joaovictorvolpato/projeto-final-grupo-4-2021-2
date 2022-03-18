from abc_renderer import AbcRenderer
import pygame


class MenuRenderer(AbcRenderer):
    def __init__(self, screen_size: int, menu):
        self._size = screen_size
        self._win = pygame.display.set_mode((screen_size, screen_size))
        self._menu = menu

    def render(self):
        bg = pygame.transform.scale(self._menu.bg, (self._size, self._size))

        self._win.blit(bg, (0, 0))

        for button in self._menu.buttons:
            self._win.blit(button.img, (button.rect.x, button.rect.y))
