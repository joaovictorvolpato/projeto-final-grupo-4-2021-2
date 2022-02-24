import pygame
import sys
import math
import copy
from abc_command_object import Command_object
from abc_kinetic_object import Kinetic_object


class Player(Kinetic_object, Command_object):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int, obstacles: list):
        super().__init__(initial_x, initial_y, size, speed)
        # sprites
        self.__size = size
        self.__color = (250, 160, 60)
        self.__speed = speed
        self.__commands = {'up': False, 'down': False,
                           'right': False, 'left': False}
        self.__rect = pygame.Rect(initial_x, initial_y, size, size)
        self.__velX = 0
        self.__velY = 0
        # usar depois para mudar sprite
        self.__facing_direction = 'down'
        self.__obstacles = obstacles

    @property
    def rect(self):
        return self.__rect

    @property
    def velX(self):
        return self.__velX

    @property
    def velY(self):
        return self.__velY

    @property
    def commands(self):
        return self.__commands

    @property
    def size(self):
        return self.__size

    @property
    def color(self):
        return self.__color

    @commands.setter
    def commands(self, new_commands: dict):
        self.__commands = new_commands

    # usar para normalizar os vetores de velocidade, caso contrario, anda mais rápido nas diagonais
    def normalize(self):
        if self.__velX != 0 and self.__velY != 0:
            self.__velX *= 1/math.sqrt(2)
            self.__velY *= 1/math.sqrt(2)

    # desenha um retangulo com offset para cameta
    def draw(self, win, offset):
        fake_rect = copy.deepcopy(self.__rect)
        fake_rect.topleft -= offset
        pygame.draw.rect(win, self.__color, fake_rect)
        
    # Colisoes, funciona se nao colidir com objetos em movimento
    def move(self):
        self.normalize()
        self.__rect.x += self.__velX
        self.check_collisions('horizontal')
        self.__rect.y += self.__velY
        self.check_collisions('vertical')

    def check_collisions(self, direction):
        if direction == 'horizontal':
            for obstacle in self.__obstacles:
                if obstacle.rect.colliderect(self.__rect):
                    if self.__velX > 0: # direita
                        self.__rect.right = obstacle.rect.left
                    elif self.__velX < 0: # esquerda
                        self.__rect.left = obstacle.rect.right

        if direction == 'vertical':
            for obstacle in self.__obstacles:
                if obstacle.rect.colliderect(self.__rect):
                    if self.__velY > 0: # baixo
                        self.__rect.bottom = obstacle.rect.top
                    elif self.__velY < 0: # cima
                        self.__rect.top = obstacle.rect.bottom

            

    def change_facing_direction(self):
        # so apertando para direita
        if self.__commands['right'] and not (self.__commands['down'] or self.__commands['up'] or self.__commands['left']):
            self.__facing_direction = 'right'
        # so apertando para esquerda
        elif self.__commands['left'] and not (self.__commands['down'] or self.__commands['up'] or self.__commands['right']):
            self.__facing_direction = 'left'
        # so apertando para cima
        elif self.__commands['up'] and not (self.__commands['down'] or self.__commands['right'] or self.__commands['left']):
            self.__facing_direction = 'up'
        # so apertando para baixo
        elif self.__commands['down'] and not (self.__commands['up'] or self.__commands['left'] or self.__commands['right']):
            self.__facing_direction = 'down'

    def execute_commands(self):
        self.change_facing_direction()
        self.__velX = 0
        self.__velY = 0
        if self.__commands['left'] and not self.__commands['right']:
            self.__velX = -self.__speed
        if self.__commands['right'] and not self.__commands['left']:
            self.__velX = self.__speed
        if self.__commands['up'] and not self.__commands['down']:
            self.__velY = -self.__speed
        if self.__commands['down'] and not self.__commands['up']:
            self.__velY = self.__speed
