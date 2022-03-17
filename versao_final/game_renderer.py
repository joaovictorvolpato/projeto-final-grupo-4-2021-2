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

        # desenha objetos do jogo
        self._offset.x = self._game_state.player.rect.centerx - \
            self._win.get_size()[0] / 2
        self._offset.y = self._game_state.player.rect.centery - \
            self._win.get_size()[1] / 2
        for i in self._game_state.objects:
            self._draw(i)

        # desenha ui, precisa ser desenhada dps dos objetos do jogo
        self.__draw_health_bar()

    def _draw(self, game_obj):
        fake_rect = copy.deepcopy(game_obj.rect)
        fake_rect.topleft -= self._offset
        pygame.draw.rect(self._win, game_obj.color, fake_rect)

    def __draw_health_bar(self):
        MAXHEALTH = self._game_state.player.max_health
        CURRENT_HEALTH = self._game_state.player.current_health
        POSITIONX = 10
        POSITIONY = 20
        HEIGHT = 10
        empty_healthbar = pygame.Rect(
            POSITIONX, POSITIONY, round(MAXHEALTH * 0.6), HEIGHT)
        current_life = pygame.Rect(
            POSITIONX, POSITIONY, round(CURRENT_HEALTH * 0.6), HEIGHT)

        pygame.draw.rect(self._win, (0, 0, 0), empty_healthbar)
        pygame.draw.rect(self._win, (0, 255, 0), current_life)
