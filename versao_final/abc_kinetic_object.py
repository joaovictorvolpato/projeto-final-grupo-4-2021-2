from abc import ABC, abstractmethod
from abc_object import ABCObject


class Kinetic_object(ABCObject, ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int, color: tuple, speed: int):
        ABCObject.__init__(self, initial_x, initial_y, size, color)
        self._speed = speed
        self._velX = 0
        self._velY = 0
        self._has_collided = False

    @property
    def speed(self):
        return self._speed

    @property
    def velX(self):
        return self._velX

    @property
    def velY(self):
        return self._velY

    @velX.setter
    def velX(self, new_velX):
        if isinstance(new_velX, (int, float)):
            self._velX = new_velX

    @velY.setter
    def velY(self, new_velY):
        if isinstance(new_velY, (int, float)):
            self._velY = new_velY

    @speed.setter
    def speed(self, new_speed):
        if isinstance(new_speed, int):
            self._speed = new_speed

    @abstractmethod
    def move_request(self):
        pass

    @abstractmethod
    def handle_collision(self):
        pass
