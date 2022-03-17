from os import PRIO_PGRP
import pygame
import sys


class MenuLogic:
    def __init__(self, menu):
        self._menu = menu
        self._clicked = False
        self._next_state = None

    def check_clicks(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._clicked = True
            else:
                self._clicked = False

            mx, my = pygame.mouse.get_pos()

            for button in self._menu.buttons:
                if button.collidepoint((mx, my)) and self._clicked:
                    self._next_state = button.destination

    @property
    def next_state(self):
        return self._next_state
