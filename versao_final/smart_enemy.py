import math
from abc_kinetic_object import Kinetic_object
from abc_interactable_object import Interactable_object


class Smart_enemy(Kinetic_object, Interactable_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int, player):
        Kinetic_object.__init__(self, initial_x, initial_y,
                                size, (250, 0, 0), speed)
        Interactable_object.__init__(self)
        # usar depois para mudar sprite
        self._player = player

    def move_to_player(self):
        dx, dy = self._player.rect.x - self.rect.x, self._player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        try:
            dx, dy = dx / dist, dy / dist
        except ZeroDivisionError:
            pass
        velx = dx * self.speed
        vely = dy * self.speed
        return velx, vely

    def move_request(self):
        self._velX, self._velY = self.move_to_player()
        return (self._velX, self.velY)

    def handle_collision(self, axis):
        if axis == 'horizontal':
            self._velX *= -1
        if axis == 'vertical':
            self._velY *= -1

    def on_contact(self):
        print('player collisio')
 