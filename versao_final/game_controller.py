import pygame
from game_renderer import GameRenderer
from command_handler import CommandHandler
from movement_handler import MovementHandler
from event_object_handler import EventObjectHandler
from interaction_handler import InteractionHandler
from request_analyser import RequestAnalyser
import pygame
from abc_state import AbcState


class GameController(AbcState):
    def __init__(self, screen_size):
        super().__init__('game')
        self.__renderer = GameRenderer(screen_size)
        self.__command_handler = CommandHandler()
        self.__movement_handler = MovementHandler()
        self.__event_object_handler = EventObjectHandler()
        self.__interaction_handeler = InteractionHandler()
        self.__request_analyser = RequestAnalyser()

    def state_routine(self):

        self.__request_analyser.handle_requests()

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

        self.__event_object_handler.handle_events()

        self.__interaction_handeler.handle_interaction()
