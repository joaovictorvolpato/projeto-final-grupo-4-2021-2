from os.path import join
from abc_menu import AbcMenu
from menu_button import MenuButton


class MainMenu(AbcMenu):
    def __init__(self):
        start_game_button_image_path = \
            join('images', 'start_game_button_main_menu.png')
        start_game_button = MenuButton(
            start_game_button_image_path,
            'level_selection',
            436,
            507
        )
        quit_button_image_path = join('images', 'quit_button_main_menu.png')
        quit_button = MenuButton(
            quit_button_image_path,
            'quit',
            436,
            616
        )
        buttons = [start_game_button, quit_button]
        background_path = join('images', 'background_main_menu.png')
        name = 'main'
        super().__init__(buttons, background_path, name)
