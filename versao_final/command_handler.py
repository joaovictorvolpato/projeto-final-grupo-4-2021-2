from multiprocessing import Event
from game_state import GameState
from event_handler import EventHandler
import pygame
import sys


class CommandHandler:
    def __init__(self):
        # Já havia sido instanciado pelo renderer
        self.__game_state = GameState(1)
        self.__event_handler = EventHandler()

    def execute(self):
        # checa os comandos que querem ser executados
        self.__event_handler.key_checker()
        # fecha a janela, terminando o programa, caso comando quit
        if self.__event_handler.output['quit'] == True:
            pygame.quit()
            sys.exit()
        # faz os command _objects executarem os comandos
        for command_object in self.__game_state.command_objects:
            OUTPUT = self.__event_handler.output
            command_object.change_commands(OUTPUT)
            command_object.execute_commands()
