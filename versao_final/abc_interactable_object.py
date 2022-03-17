from abc_object import ABCObject
from abc import ABC, abstractmethod
# faz alguma coisa ao colidir com o player, ex: pickup, inimigos


class Interactable_object(ABC):

    # oque o objeto faz quando entra em contato com o player
    @abstractmethod
    def on_contact(self):
        pass
