from abc_object import ABCObject
from abc import ABC, abstractmethod
class Event_object(ABCObject, ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int):
        super().__init__(initial_x, initial_y, size)

    @abstractmethod
    def trigger_event(self):
        pass

    @abstractmethod
    def check_player_collisions(self):
        pass