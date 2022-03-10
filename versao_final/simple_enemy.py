import math
from abc_kinetic_object import Kinetic_object
from abc_interactable_object import Interactable_object


class Simple_enemy(Kinetic_object, Interactable_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        Kinetic_object.__init__(self, initial_x, initial_y,
                                size, (250, 0, 0), speed)
        Interactable_object.__init__(self)
        # usar depois para mudar sprite
        self._facing_direction = 'right'
        self._velX = self.speed*0.5
        self._velY = self.speed*0.25

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
        print('player collision')
