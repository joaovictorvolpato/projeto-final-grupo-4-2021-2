from os.path import join
from abc_menu import AbcMenu
from menu_button import MenuButton


class WinMenu(AbcMenu):
    """
    Represents the screen for when the player wins the game.
    """

    def __init__(self):
        return_button_image_path = \
            join('images', 'return_to_menu_button.png')
        return_to_menu_button = \
            MenuButton(return_button_image_path, 'main', 334, 520)
        quit_button_image_path = \
            join('images', 'quit_button_large.png')
        quit_button = \
            MenuButton(quit_button_image_path, 'quit', 395, 670)
        buttons = [return_to_menu_button, quit_button]
        background_path = join('images', 'background_victory_screen.png')
        name = 'win'
        super().__init__(buttons, background_path, name)
