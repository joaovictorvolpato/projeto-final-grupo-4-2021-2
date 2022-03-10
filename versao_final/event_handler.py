import pygame
import sys
# Transforma inputs em comandos para o jogo


class Event_handler:
    def __init__(self):
        # teclas que fazem coisas no jogo, USAR PARA TIRAR IFS DPS
        self.__event_list = ([pygame.QUIT, pygame.KEYDOWN, pygame.K_RIGHT,
                              pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.KEYUP, pygame.K_SPACE])
        # output desss teclas
        self.__output = {'up': False, 'down': False,
                         'right': False, 'left': False, 'quit': False, 'space_bar': False}

    # getters
    @property
    def output(self):
        return self.__output

    # cuida de novos eventos, modificando os outputs

    # da para tirar esses ifs depois se der tempo
    def key_checker(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__output['quit'] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.__output['left'] = True
                if event.key == pygame.K_RIGHT:
                    self.__output['right'] = True
                if event.key == pygame.K_UP:
                    self.__output['up'] = True
                if event.key == pygame.K_DOWN:
                    self.__output['down'] = True
                if event.key == pygame.K_SPACE:
                    self.__output['space_bar'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.__output['left'] = False
                if event.key == pygame.K_RIGHT:
                    self.__output['right'] = False
                if event.key == pygame.K_UP:
                    self.__output['up'] = False
                if event.key == pygame.K_DOWN:
                    self.__output['down'] = False
                if event.key == pygame.K_SPACE:
                    self.__output['space_bar'] = False
