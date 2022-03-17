import math
from abc_kinetic_object import Kinetic_object
from abc_interactable_object import Interactable_object
from abc_request_object import AbcRequestObject


class Smart_enemy(Kinetic_object, Interactable_object, AbcRequestObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        Kinetic_object.__init__(self, initial_x, initial_y,
                                size, (250, 0, 0), speed)
        Interactable_object.__init__(self)
        AbcRequestObject.__init__(self, ['player'])
        self._player = None
        # usar depois para mudar sprite
        self._dano = 5

    def move_request(self):
        player = self._player
        print(player.rect.x, player.rect.y)
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        try:
            dx, dy = dx / dist, dy / dist
        except ZeroDivisionError:
            print('dividiu por zero ;-;')
        self._velX = dx * self.speed
        self._velY = dy * self.speed
        return (self._velX, self.velY)

    def handle_collision(self, axis):
        if axis == 'horizontal':
            self._velX *= -1
        if axis == 'vertical':
            self._velY *= -1

    def on_contact(self):
        self._player.health -= self._dano

    def use_request(self, requested: list):
        self._player = requested[0]

    def request_to_gs(self):
        return {'player': self._player}
