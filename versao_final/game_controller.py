from tkinter import Menu
import pygame
from game_renderer import GameRenderer
from command_handler import CommandHandler
from menu_controller import MenuController
from movement_handler import MovementHandler
from event_object_handler import EventObjectHandler
from interaction_handler import InteractionHandler
from request_analyser import RequestAnalyser
import pygame
from abc_state import AbcState
from vitctory_lost_handler import VictoryLostHandler


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
        self._won_game = False
        self._lost_game = False

    def state_routine(self):

        self.__request_analyser.handle_requests()

        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

        self.__event_object_handler.handle_events()

        self.__interaction_handeler.handle_interaction()

        lost = self.__victory_lost_handeler.check_if_lost()

        self.lost_game = lost
        if self.lost_game:
            self._next_state = MenuController

        won = self.__victory_lost_handeler.check_if_won()

        self.won_game = won
        if self._won_game:
            self._next_state = MenuController



    @property
    def won_game(self):
        return self._won_game

    @property
    def lost_game(self):
        return self._lost_game

    @won_game.setter
    def won_game(self, value):
        self._won_game = value

    @lost_game.setter
    def lost_game(self, value):
        self._lost_game = value



