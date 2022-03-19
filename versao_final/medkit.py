from abc_object import ABCObject
from abc_interactable_object import InteractableObject


class Medkit(ABCObject, InteractableObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, sprite: str):
        super().__init__(initial_x, initial_y, size, sprite)
        self._heal = 300
        self._active = True

    def on_contact(self):
        if self._active == True:
            self.change_sprite('sprites/nothing.png')
            self._active = False
            return {'heal': 300}
