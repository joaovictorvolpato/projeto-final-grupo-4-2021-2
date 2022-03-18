import math
import time
from abc_object import ABCObject
from abc_interactable_object import InteractableObject


class FreezEnemy(ABCObject, InteractableObject):
    def __init__(self, initial_x: int, initial_y: int, size: int, ):
        ABCObject.__init__(self, initial_x, initial_y,
                           size, 'sprites/ice.png')
        InteractableObject.__init__(self)
        # self._player = None
        # usar depois para mudar sprite
        # self._slow_player = False
        self._speed_loss = 100

    '''def move_request(self):
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
            self._velY *= -1'''

    def on_contact(self):
        return {'slow': self._speed_loss}

    # def use_request(self, requested: list):
    #     self._player = requested[0]

    # # def request_to_gs(self):
    # #     if self._slow_player == True:
    # #         self._slow_player = False
