from abc import ABC, abstractmethod


class AbcRequestObject(ABC):
    def __init__(self, request: list):
        # requere informações do game state
        self._request = request

    @abstractmethod
    def use_request(self, requested: list):
        pass

    @property
    def request(self):
        return self._request
