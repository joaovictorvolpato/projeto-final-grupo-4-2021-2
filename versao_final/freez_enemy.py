import math
import time
from abc_object import ABCObject
from abc_interactable_object import InteractableObject


class FreezEnemy(ABCObject, InteractableObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, sprite: str):
        ABCObject.__init__(self, initial_x, initial_y,
                           size, sprite)
        InteractableObject.__init__(self)

        self._speed_loss = 100

    def on_contact(self):
        return {'slow': self._speed_loss}
