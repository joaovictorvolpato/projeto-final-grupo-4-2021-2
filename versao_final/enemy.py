import pygame
import math
from abc_kinetic_object import Kinetic_object


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


    def move(self):
        self._rect.x += self._velX
        self._rect.y += self._velY
        self.check_collisions()


    def check_collisions(self):
        for obstacle in self._obstacles:
            if obstacle.rect.colliderect(self._rect):
                print(self.velX)
                if self._velX > 0:  # direita
                    self._rect.right = obstacle.rect.left
                    print("colidiu direita")
                    self.change_directionsX()
                elif self._velX < 0:  # esquerda
                    self._rect.left = obstacle.rect.right
                    print("colidiu esquerda")
                    self.change_directionsX()

        for obstacle in self._obstacles:
            if obstacle.rect.colliderect(self._rect):
                if self._velY > 0:  # baixo
                    self._rect.bottom = obstacle.rect.top
                    print("colidiu baixo")
                    self.change_directionsY()
                elif self._velY < 0:  # cima
                    self._rect.top = obstacle.rect.bottom
                    print("colidiu cima")
                    self.change_directionsY()


    def change_directionsX(self):
        self._velX = -1 * self._velX

    def change_directionsY(self):
        self._velY = -1 *self._velY 
