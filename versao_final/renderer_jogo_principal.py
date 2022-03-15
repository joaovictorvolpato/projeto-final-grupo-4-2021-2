from game_state import Game_state
import pygame
import copy
from renderer import Renderer

class RendererJogoPrincipal(Renderer):
    def __init__(self):
        # singleton, vai ser o primeiro a inicializar o game_state, com o nivel inicial
        self.__game_state = Game_state()
        self.__offset = pygame.Vector2()

    def render(self):
        self.__game_state.win.fill((12, 24, 36))
        self.__offset.x = self.__game_state.player.rect.centerx - \
            self.__game_state.win.get_size()[0] / 2
        self.__offset.y = self.__game_state.player.rect.centery - \
            self.__game_state.win.get_size()[1] / 2
        for i in self.__game_state.objects:
            self.__draw(i)

    def __draw(self, game_obj):
        fake_rect = copy.deepcopy(game_obj.rect)
        fake_rect.topleft -= self.__offset
        pygame.draw.rect(self.__game_state.win, game_obj.color, fake_rect)

