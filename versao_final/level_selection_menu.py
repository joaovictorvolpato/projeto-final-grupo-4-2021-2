from os.path import join
from abc_menu import AbcMenu
from menu_button import MenuButton
from level_button import LevelButton


class LevelSelectionMenu(AbcMenu):
    """
    Represents the level-selection menu.
    """

    def __init__(self):
        return_image_path = join(
            "images",
            "return_button_level_selection.png"
        )
        buttons = [
                MenuButton(return_image_path, "main", 126, 157),
                LevelButton(1, 160, 325),
                LevelButton(2, 643, 480),
                LevelButton(3, 162, 546),
                ]
        background_path = \
            join("images", "background_level_selection_menu.png")
        name = "level_selection"
        super().__init__(buttons, background_path, name)
