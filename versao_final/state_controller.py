from tkinter import Menu
from menu_logic import MenuLogic
from menu_renderer import MenuRenderer
from main_menu import MainMenu
from options_menu import OptionsMenu


class MenuController:
    def __init__(self, screen_size: int):
        self._states = [MainMenu(), OptionsMenu()]
        self._current_state = MainMenu()
        self.menu_logic = MenuLogic(self._current_state)
        self.menu_renderer = MenuRenderer(screen_size, self._current_state)

    def main_loop()
