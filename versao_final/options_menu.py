from abc_menu import AbcMenu
from menu_button import MenuButton


class OptionsMenu(AbcMenu):
    def __init__(self, buttons: list, background: str, name: str):
        super().__init__([MenuButton('sprites/start.png', 'game', 500, 300),
                          MenuButton('sprites/exit.png', 'quit', 100, 300)],
                         'sprites/background_colorido.jpg', 'options')
