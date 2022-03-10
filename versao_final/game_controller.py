import pygame
import sys
from renderer import Renderer
from command_handler import Command_handler
from movement_handler import Movement_handler
from event_object_handler import Event_object_handler
from interaction_handler import Interaction_handler
import pygame


class Game_controller:
    def __init__(self, screen_size):
        self.__renderer = Renderer(screen_size)
        self.__command_handler = Command_handler()
        self.__movement_handler = Movement_handler()
        self.__event_object_handler = Event_object_handler()
        self.__interaction_handler = Interaction_handler()

    def execute_game_routine(self):

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

        self.__event_object_handler.handle_event()

        self.__interaction_handler.handle_interaction()
