from this import d
from abc_object import ABCObject
from abc import ABC, abstractmethod


class Event_object(ABCObject, ABC):
    def __init__(self, initial_x: int, initial_y: int, size: int, color: tuple):
        super().__init__(initial_x, initial_y, size, color)

    @abstractmethod
    def trigger_event(self):
        pass
