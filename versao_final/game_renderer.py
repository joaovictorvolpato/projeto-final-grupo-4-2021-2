from abc_renderer import AbcRenderer
from game_state import GameState
import pygame
import copy


class GameRenderer(AbcRenderer):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        # singleton, vai ser o primeiro a inicializar o game_state, com o nivel inicial
        self._game_state = GameState(1)
        self._offset = pygame.Vector2()

    def render(self):
        self._win.fill((12, 24, 36))
        self._offset.x = self._game_state.player.rect.centerx - \
            self._win.get_size()[0] / 2
        self._offset.y = self._game_state.player.rect.centery - \
            self._win.get_size()[1] / 2
        for i in self._game_state.objects:
            self._draw(i)

    def _draw(self, game_obj):
        fake_rect = copy.deepcopy(game_obj.rect)
        fake_rect.topleft -= self._offset
        pygame.draw.rect(self._win, game_obj.color, fake_rect)
