from abc import ABC, abstractmethod
# faz alguma coisa ao colidir com o player, ex: pickup, inimigos


class InteractableObject(ABC):

    # oque o objeto faz quando entra em contato com o player
    @abstractmethod
    def on_contact(self):
        pass
