import math

from abc_kinetic_object import KineticObject
from abc_interactable_object import InteractableObject
import random


class SimpleEnemy(KineticObject, InteractableObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int, sprite: str):
        KineticObject.__init__(self, initial_x, initial_y,
                               size, sprite, speed)
        InteractableObject.__init__(self)
        # usar depois para mudar sprite
        self._facing_direction = 'right'
        self._velX = self.speed * (random.randint(-10, 10)/10)
        self._velY = self.speed * (random.randint(-10, 10)/10)
        self._dano = 100

    def normalize(self):
        if self._velX != 0 and self._velY != 0:
            self._velX *= 1/math.sqrt(2)
            self._velY *= 1/math.sqrt(2)

    def move_request(self):
        return (self._velX, self._velY)

    def handle_collision(self, axis):
        if axis == 'horizontal':
            self._velX *= -1
        if axis == 'vertical':
            self._velY *= -1

    def on_contact(self):
        return {'hit': self._dano}
