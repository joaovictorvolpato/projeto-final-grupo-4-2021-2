from menu_logic import MenuLogic
from menu_renderer import MenuRenderer
from main_menu import MainMenu
from options_menu import OptionsMenu
import pygame
from abc_state import AbcState


class MenuController(AbcState):
    def __init__(self, screen_size: int):
        super().__init__('menu')
        self._clk = pygame.time.Clock()
        self._screen_size = screen_size
        self._menus = [MainMenu(), OptionsMenu()]
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
            if self._menu_logic.next_menu == 'quit' or self._menu_logic.next_menu == 'game':
                self._next_state = self._menu_logic.next_menu

            # procurar menu com esse nome e botar ele como current
            for menu in self._menus:
                if menu.name == self._menu_logic.next_menu:
                    self._current_menu = menu
                    self._menu_logic = MenuLogic(menu)
                    self._menu_renderer = MenuRenderer(
                        self._screen_size, menu)
