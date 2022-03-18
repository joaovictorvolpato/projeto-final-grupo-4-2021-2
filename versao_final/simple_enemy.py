import math

from abc_kinetic_object import KineticObject
from abc_interactable_object import InteractableObject
from abc_request_object import AbcRequestObject


class SimpleEnemy(KineticObject, InteractableObject, AbcRequestObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        KineticObject.__init__(self, initial_x, initial_y,
                               size, 'sprites/vacuum.png', speed)
        InteractableObject.__init__(self)
        AbcRequestObject.__init__(self, ['player'])
        # usar depois para mudar sprite
        self._facing_direction = 'right'
        self._velX = self.speed*0.5
        self._velY = self.speed*0.25
        self._dano = 5

        self._fake_player = None
        self._deal_damage = False

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
        self._deal_damage = True

    def use_request(self, requested: list):
        self._fake_player = requested[0]

    def request_to_gs(self):
        if self._deal_damage == True:
            self._deal_damage = False
            return {'damage': self._dano}
