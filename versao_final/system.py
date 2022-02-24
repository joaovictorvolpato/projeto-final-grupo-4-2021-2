import pygame
from game_controller import Game_controller


class System:
    def __init__(self, size, title, clk_speed):
        self.__size = size
        self.__title = title
        self.__clk_speed = clk_speed
        self.__clk = pygame.time.Clock()
        self.__game_controller = Game_controller(self.__size)

    def initialize(self):
        pygame.init()
        pygame.display.set_caption(self.__title)
        self.main_loop()

        
    def main_loop(self):
        while True:
            # comandos
            self.__game_controller.execute_all_commands()
    
            # movimentos e colisoes
            self.__game_controller.move_all()

            # eventos
            self.__game_controller.check_all_events_obj()

            # Draw
            self.__game_controller.draw_all()

            # update o display inteiro e fps
            pygame.display.flip()
            self.__clk.tick(self.__clk_speed)