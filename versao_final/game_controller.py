from tkinter import Menu
import pygame
from game_renderer import GameRenderer
from command_handler import CommandHandler
from movement_handler import MovementHandler
from event_object_handler import EventObjectHandler
from interaction_handler import InteractionHandler
from request_analyser import RequestAnalyser
import pygame
from abc_state import AbcState
from vitctory_lost_handler import VictoryLostHandler
from game_state import GameState


class GameController(AbcState):
    def __init__(self, screen_size):
        super().__init__('game')
        self.__renderer = GameRenderer(screen_size)
        self.__command_handler = CommandHandler()
        self.__movement_handler = MovementHandler()
        self.__event_object_handler = EventObjectHandler()
        self.__interaction_handeler = InteractionHandler()
        self.__request_analyser = RequestAnalyser()
        self.__victory_lost_handeler = VictoryLostHandler()
        self._next_state = None

    def state_routine(self):

        self.__request_analyser.handle_requests()

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

        self.__interaction_handeler.handle_interaction()

        self.__event_object_handler.handle_events()

        self._next_state = self.__victory_lost_handeler.check_situation()

    def change_semi_state(self, next_level):
        pass
