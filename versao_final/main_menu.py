from abc_menu import AbcMenu
from menu_button import MenuButton


class MainMenu(AbcMenu):
    def __init__(self):
        super().__init__([MenuButton('sprites/start.png', 'options', 300, 300),
                          MenuButton('sprites/exit.png', 'game', 400, 300)],
                         'sprites/background_colorido.jpg', 'main')
