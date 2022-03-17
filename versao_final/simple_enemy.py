import math

from abc_kinetic_object import KineticObject
from abc_interactable_object import InteractableObject
from abc_request_object import AbcRequestObject


class SimpleEnemy(KineticObject, InteractableObject, AbcRequestObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        KineticObject.__init__(self, initial_x, initial_y,
                                size, (250, 0, 0), speed)
        InteractableObject.__init__(self)
        AbcRequestObject.__init__(self, ['player'])
        # usar depois para mudar sprite
        self._facing_direction = 'right'
        self._velX = self.speed*0.5
        self._velY = self.speed*0.25
        self.dano = 5

        self._player = None

    def normalize(self):
        if self._velX != 0 and self._velY != 0:
            self._velX *= 1/math.sqrt(2)
            self._velY *= 1/math.sqrt(2)

    def move_request(self):
        return (self._velX, self.velY)

    def handle_collision(self, axis):
        if axis == 'horizontal':
            self._velX *= -1
        if axis == 'vertical':
            self._velY *= -1

    def on_contact(self):
        self._player.health -= self.dano

    def use_request(self, requested: list):
        self._player = requested[0]

    def request_to_gs(self):
        return {'player': self._player}
