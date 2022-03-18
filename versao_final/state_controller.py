from menu_controller import MenuController
from game_controller import GameController
import pygame


class StateController:

    def __init__(self):
        pygame.init()
        self.__screen_size = 1000
        self.__clk = pygame.time.Clock()
        self.__states = [MenuController(self.__screen_size, 'main'),
                         GameController(self.__screen_size)]
        self.__current_state = self.__states[0]

    def main_loop(self):
        while True:
            self.__current_state.state_routine()

            if not self.__current_state.next_state is None:
                for state in self.__states:
                    if state.name == self.__current_state.next_state[0]:
                        next_semi_state = self.__current_state.next_state[1]
                        self.__current_state = state
                        self.__current_state.change_semi_state(next_semi_state)
                        break

            pygame.display.flip()
            self.__clk.tick(60)

    def initialize(self):
        pygame.display.set_caption('jogo legal')
        self.main_loop()
