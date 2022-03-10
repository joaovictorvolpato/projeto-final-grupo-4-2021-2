from abc_object import ABCObject
from abc import ABC, abstractmethod
# faz alguma coisa ao colidir com o player, ex: pickup, inimigos


class Interactable_object(ABCObject, ABC):
    def __init__(self):
        pass

    @abstractmethod
    def on_contact(self):
        pass
