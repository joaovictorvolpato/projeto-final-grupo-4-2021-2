from abc import ABC, abstractmethod

class CarregadorDeDados(ABC):
    """
    Esta classe funciona como uma interface que os componentes
    carregadores de dados apresentam.
    """
    @abstractmethod
    def carregar(self):
        pass

    @abstractmethod
    def limpar(self):
        pass

