import math
from abc_command import Command
from abc_kinetic_object import KineticObject


class Player(KineticObject, Command):
    def __init__(self, initial_x: int, initial_y: int, size: int, speed: int):
        KineticObject.__init__(
            self, initial_x, initial_y, size, 'sprites/placeholder.png',  speed)
        Command.__init__(
            self, {'up': False, 'down': False, 'right': False, 'left': False, 'space_bar': False})
        # usar depois para mudar sprite
        self._facing_direction = 'down'
        # interagir com objetos próximos
        self._is_interacting = False
        self._interactable_radius = self._size + self._size/3
        self._max_health = 500
        self._current_health = self._max_health
        self._has_lost = False
        self._has_won = False

        # tempo ate acabar freeze

    @property
    def interactable_radius(self):
        return self._interactable_radius

    @property
    def max_health(self):
        return self._max_health

    @property
    def current_health(self):
        return self._current_health

    @property
    def has_won(self):
        return self._has_won

    @property
    def has_lost(self):
        return self._has_lost

    @has_won.setter
    def has_won(self, value):
        self._has_won = value

    @has_lost.setter
    def has_lost(self, value):
        self._has_lost = value

    @current_health.setter
    def current_health(self, new):
        if isinstance(new, int):
            self._current_health = new

    # usar para normalizar os vetores de velocidade, caso contrario, anda mais rápido nas diagonais
    @property
    def is_interacting(self):
        return self._is_interacting

    def __normalize(self):
        if self._velX != 0 and self._velY != 0:
            self._velX *= 1/math.sqrt(2)
            self._velY *= 1/math.sqrt(2)

    def move_request(self):

        return(self._velX, self._velY)

    def handle_collision(self, axis):
        # fazer alguma coisa legal aqui dps
        pass

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
        self._is_interacting = self._commands['space_bar']
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
