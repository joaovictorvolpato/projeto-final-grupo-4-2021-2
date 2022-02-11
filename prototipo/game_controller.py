from http.client import GATEWAY_TIMEOUT
import pygame
import sys
from game_state import Game_state
from event_handler import Event_handler
import pygame
class Game_controller:
    def __init__(self, screen_size):
        self.__game_state = Game_state(screen_size/2, screen_size/2)
        self.__win = pygame.display.set_mode((screen_size, screen_size))
        self.__event_handler = Event_handler()
        self.__offset = pygame.Vector2()
    
    @staticmethod 
    def __lookForCommands(output: dict, possible_commands: dict):
        for i in output.keys():
            if i in possible_commands.keys():
                possible_commands[i] = output[i]
        return possible_commands

    def check_all_collisions(self):
        for i in self.__game_state.kinetic_objects:
                i.check_colisions(self.__game_state.obstacles)

    def update_all(self):
        for i in self.__game_state.kinetic_objects:
                i.update()

    def draw_all(self):
        self.__win.fill((12, 24, 36))
        self.__offset.x = self.__game_state.player.rect.centerx - self.__win.get_size()[0] / 2
        self.__offset.y = self.__game_state.player.rect.centery - self.__win.get_size()[1] / 2
        for i in self.__game_state.objects:
            i.draw(self.__win, self.__offset)

    def get_camera_offset(self):
        PLAYER = self.__game_state.player
        


    def execute_all_commands(self):
        self.__event_handler.key_checker()

        # Fecha a janela, termina o programa
        if (self.__event_handler.output['quit'] == True):
            pygame.quit()
            sys.exit()

        # executa os comandos dados pelo event handler
        for command_object in self.__game_state.command_objects:
            OUTPUT = self.__event_handler.output
            command_object.commands = self.__lookForCommands(OUTPUT, command_object.commands)
            command_object.execute_commands()


    #temp
    @property
    def game_state(self):
        return self.__game_state