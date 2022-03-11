from game_state import Game_state
import pygame
import copy
import os
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 40)
WHITE = (255,255,255)




class Renderer:
    def __init__(self, screen_size):
        # singleton, vai ser o primeiro a inicializar o game_state, com o nivel inicial
        self.screen_size = screen_size
        self.__game_state = Game_state(1)
        self.__win = pygame.display.set_mode((screen_size, screen_size))
        self.__offset = pygame.Vector2()

    def draw_text(self):
        self.__game_state = Game_state(1)
        player_health_text = FONT.render("VIDA:" + str(self.__game_state.player.health), 1, WHITE)
        self.__win.blit(player_health_text,(self.__game_state.player.rect))

    def render(self):
        self.draw_text()
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
