from game_state import Game_state
import pygame
import copy


class Renderer:
    def __init__(self, screen_size):
        # singleton, vai ser o primeiro a inicializar o game_state, com o nivel inicial
        self.__game_state = Game_state(1)
        self.__win = pygame.display.set_mode((screen_size, screen_size))
        self.__offset = pygame.Vector2()

    def render(self):
        self.__win.fill((12, 24, 36))
        self.__offset.x = self.__game_state.player.rect.centerx - \
            self.__win.get_size()[0] / 2
        self.__offset.y = self.__game_state.player.rect.centery - \
            self.__win.get_size()[1] / 2
        for i in self.__game_state.objects:
            self.__draw(i)

    def __draw(self, game_obj):
        fake_rect = copy.deepcopy(game_obj.rect)
        fake_rect.topleft -= self.__offset
        pygame.draw.rect(self.__win, game_obj.color, fake_rect)


# def draw_all(self):
#         self.__win.fill((12, 24, 36))
#         self.__offset.x = self.__game_state.player.rect.centerx - \
#             self.__win.get_size()[0] / 2
#         self.__offset.y = self.__game_state.player.rect.centery - \
#             self.__win.get_size()[1] / 2
#         for i in self.__game_state.objects:
#             i.draw(self.__win, self.__offset)
