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

    def execute_game_routine(self):

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()
