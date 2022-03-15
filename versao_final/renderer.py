from abc import ABC, abstractmethod

class Renderer(ABC):
    """
    Esta classe funciona como uma interface que os rederizadores devem
    apresentar.
    """
    @abstractmethod
    def render(self):
        pass

