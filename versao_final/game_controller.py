import pygame
import sys
from renderer import Renderer
from command_handler import Command_handler
from movement_handler import Movement_handler
import pygame


class Game_controller:
    def __init__(self, screen_size):
        self.__renderer = Renderer(screen_size)
        self.__command_handler = Command_handler()
        self.__movement_handler = Movement_handler()
        # self.__win = pygame.display.set_mode((screen_size, screen_size))
        # self.__offset = pygame.Vector2()

    def execute_game_routine(self):

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

    # @staticmethod
    # def __lookForCommands(output: dict, possible_commands: dict):
    #     for i in output.keys():
    #         if i in possible_commands.keys():
    #             possible_commands[i] = output[i]
    #     return possible_commands

    # def move_all(self):
    #     for i in self.__game_state.kinetic_objects:
    #         i.move()

    # def draw_all(self):
    #     self.__win.fill((12, 24, 36))
    #     self.__offset.x = self.__game_state.player.rect.centerx - \
    #         self.__win.get_size()[0] / 2
    #     self.__offset.y = self.__game_state.player.rect.centery - \
    #         self.__win.get_size()[1] / 2
    #     for i in self.__game_state.objects:
    #         i.draw(self.__win, self.__offset)

    # def check_enemy_player_all(self):
    #     for i in self.__game_state.enemies:
    #         i.check_player_collision(self.__game_state.player.rect)

        #  implementar dps para camera para de seguir perto das paredes
        # def get_camera_offset(self):
        #     PLAYER = self.__game_state.player

    # def check_all_events_obj(self):
    #     for i in self.__game_state.event_objects:
    #         output = i.check_player_collisions(self.__game_state.player)
    #         # mudar para checar inteiro dps asdflkj
    #         if output == 1 or output == 2:
    #             self.__game_state.change_level(output)

    # def execute_all_commands(self):
    #     self.__event_handler.key_checker()

    #     # Fecha a janela, termina o programa
    #     if (self.__event_handler.output['quit'] == True):
    #         pygame.quit()
    #         sys.exit()

    #     # executa os comandos dados pelo event handler
    #     for command_object in self.__game_state.command_objects:
    #         OUTPUT = self.__event_handler.output
    #         command_object.change_commands(OUTPUT)
    #         command_object.execute_commands()
