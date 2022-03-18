from menu_logic import MenuLogic
from menu_renderer import MenuRenderer
from main_menu import MainMenu
from win_menu import WinMenu
from level_selection_menu import LevelSelectionMenu
from lost_menu import LostMenu
import pygame
from abc_state import AbcState


class MenuController(AbcState):
    def __init__(self, screen_size: int):
        super().__init__('menu')
        self._clk = pygame.time.Clock()
        self._screen_size = screen_size
        self._menus = [MainMenu(), LevelSelectionMenu(), WinMenu(), LostMenu()]
        self._current_menu = self._menus[0]
        self._menu_logic = MenuLogic(self._current_menu)
        self._menu_renderer = MenuRenderer(
            self._screen_size, self._current_menu)

    def state_routine(self):

        self._menu_renderer.render()

        self._menu_logic.check_clicks()

        # checar se mudou de menu e mudar para menu apropriado
        if not self._menu_logic.next_menu is None:

            # casos especficos que nao mudam de menu mas mudam de estado
            if isinstance(self._menu_logic.next_menu, int):
                self._next_state = ['game', self._menu_logic.next_menu, ]

            # procurar menu com esse nome e botar ele como current
            self.__change_menu(self._menu_logic._next_menu)

    def __change_menu(self, next_menu):
        for next_menu_obj in self._menus:
            if next_menu == next_menu_obj.name:
                self._current_menu = next_menu_obj
                self._menu_logic = MenuLogic(next_menu_obj)
                self._menu_renderer = MenuRenderer(
                    self._screen_size, next_menu_obj)

    def change_semi_state(self, next_menu):
        self._next_state = None
        self.__change_menu(next_menu)
