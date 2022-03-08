import math
from abc_command import Command
from abc_kinetic_object import Kinetic_object


class Player(Kinetic_object, Command):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int, obstacles: list):
        Kinetic_object.__init__(
            self, initial_x, initial_y, size, (250, 160, 60),  speed)
        Command.__init__(
            self, {'up': False, 'down': False, 'right': False, 'left': False})
        # usar depois para mudar sprite
        self._facing_direction = 'down'
        self._obstacles = obstacles

    # usar para normalizar os vetores de velocidade, caso contrario, anda mais rápido nas diagonais
    def __normalize(self):
        if self._velX != 0 and self._velY != 0:
            self._velX *= 1/math.sqrt(2)
            self._velY *= 1/math.sqrt(2)

    def move_request(self):

        return(self._velX, self._velY)

    def handle_collision(self, axis):
        print('player colidiu')

    def change_facing_direction(self):
        # so apertando para direita
        if self._commands['right'] and not (self._commands['down'] or self._commands['up'] or self._commands['left']):
            self._facing_direction = 'right'
        # so apertando para esquerda
        elif self._commands['left'] and not (self._commands['down'] or self._commands['up'] or self._commands['right']):
            self._facing_direction = 'left'
        # so apertando para cima
        elif self._commands['up'] and not (self._commands['down'] or self._commands['right'] or self._commands['left']):
            self._facing_direction = 'up'
        # so apertando para baixo
        elif self._commands['down'] and not (self._commands['up'] or self._commands['left'] or self._commands['right']):
            self._facing_direction = 'down'

    def execute_commands(self):
        self.change_facing_direction()
        self._velX = 0
        self._velY = 0
        if self._commands['left'] and not self._commands['right']:
            self._velX = -self._speed
        if self._commands['right'] and not self._commands['left']:
            self._velX = self._speed
        if self._commands['up'] and not self._commands['down']:
            self._velY = -self._speed
        if self._commands['down'] and not self._commands['up']:
            self._velY = self._speed
        self.__normalize()
