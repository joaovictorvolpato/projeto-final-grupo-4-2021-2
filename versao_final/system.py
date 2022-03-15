import pygame
from game_state import Game_state
from gerenciador_de_estados import GerenciadorDeEstados

class System:
    def __init__(self, size, title, clk_speed):
        self.__size = size
        self.__title = title
        self.__clk_speed = clk_speed
        self.__clk = pygame.time.Clock()
        self.__game_state = Game_state()

    def initialize(self):
        pygame.init()
        pygame.display.set_caption(self.__title)
        self.__game_state.win = \
                pygame.display.set_mode((self.__size, self.__size))
        self.__gerenciador_de_estados = GerenciadorDeEstados()
        self.main_loop()

    def main_loop(self):
        while True:
            self.__gerenciador_de_estados.processar()

            pygame.display.flip()
            self.__clk.tick(self.__clk_speed)

