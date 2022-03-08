import pygame
import math
from abc_kinetic_object import Kinetic_object
from player import Player


class Enemy(Kinetic_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int, obstacles: list):
        super().__init__(initial_x, initial_y, size, (250, 160, 60),  speed)
        # usar depois para mudar sprite
        self._facing_direction = 'right'
        self._obstacles = obstacles
        self._velX = self.speed*0.5
        self._velY = self.speed*0.25

    def normalize(self):
        if self._velX != 0 and self._velY != 0:
            self._velX *= 1/math.sqrt(2)
            self._velY *= 1/math.sqrt(2)

    def move_request(self):
        # self._rect.x += self._velX
        # self._rect.y += self._velY
        # self.check_collisions()
        return (self._velX, self.velY)

    def handle_collision(self, axis):
        if axis == 'horizontal':
            self._velX *= -1
        if axis == 'vertical':
            self._velY *= -1

    def event(self):
        print('player collision')
