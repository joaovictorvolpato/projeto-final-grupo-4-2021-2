from menu_logic import MenuLogic
from menu_renderer import MenuRenderer
from main_menu import MainMenu
from options_menu import OptionsMenu
import pygame


class MenuController:
    def __init__(self, screen_size: int):
        self._clk = pygame.time.Clock()
        self._screen_size = screen_size
        self._menus = [MainMenu(), OptionsMenu()]
        self._current_menu = self._menus[0]
        self._menu_logic = MenuLogic(self._current_menu)
        self._menu_renderer = MenuRenderer(
            self._screen_size, self._current_menu)

    def menu_loop(self):
        while True:
            self._menu_renderer.render()

            self._menu_logic.check_clicks()

            if not self._menu_logic.next_menu is None:
                for menu in self._menus:
                    if menu.name == self._menu_logic.next_menu:
                        self._current_menu = menu
                        self._menu_logic = MenuLogic(menu)
                        self._menu_renderer = MenuRenderer(
                            self._screen_size, menu)

            pygame.display.flip()
            self._clk.tick(60)


controller = MenuController(600)
controller.menu_loop()
