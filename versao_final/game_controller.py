import pygame
from game_renderer import GameRenderer
from command_handler import Command_handler
from movement_handler import Movement_handler
from event_object_handler import Event_object_handler
from interaction_handler import Interaction_handler
from request_analyser import RequestAnalyser
import pygame
from abc_state import AbcState


class Game_controller(AbcState):
    def __init__(self, screen_size):
        super().__init__('game')
        self.__renderer = GameRenderer(screen_size)
        self.__command_handler = Command_handler()
        self.__movement_handler = Movement_handler()
        self.__event_object_handler = Event_object_handler()
        self.__interaction_handeler = Interaction_handler()
        self.__request_analyser = RequestAnalyser()

    def state_routine(self):

        self.__request_analyser.handle_requests()

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

        self.__event_object_handler.handle_events()

        self.__interaction_handeler.handle_interaction()
