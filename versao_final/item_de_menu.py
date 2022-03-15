from abc import ABC, abstractmethod
from pygame import Rect

class ItemDeMenu(ABC):
    """
    Esta classe funciona como uma interface que itens de menu simples
    apresentam.
    """
    @abstractmethod
    def desenhar(self, superficie_de_desenho):
        """
        Desenha este item de menu na superfície de desenho recebida
        como argumento.
        """
        pass

    @property
    @abstractmethod
    def area_da_superficie(self) -> Rect:
        """
        Retorna o objeto do tipo pygame.Rect com as informações sobre a
        área deste item.
        """
        pass

    @property
    @abstractmethod
    def tem_item_visivel(self) -> bool:
        """
        Informa se este item está visível na tela.
        """
        pass

