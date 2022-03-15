from abc import ABC, abstractmethod

class MensagemDePilhaDeEstados(ABC):
    """
    Esta classe funciona como uma interface que as mensagens de pilha
    de estados apresentam.
    """
    @property
    @abstractmethod
    def numero_de_estados_para_remover(self) -> int:
        """
        Retorna o número de estados que devem ser removidos da pilha
        antes de adicionar os novos estados.
        """
        pass

    @property
    @abstractmethod
    def estados_para_adicionar(self) -> list:
        """
        Retorna uma lista de instâncias dos estados de jogo que serão
        adicionados à pilha de estados.
        """
        pass

    @property
    @abstractmethod
    def esvaziar_pilha_de_estados(self) -> bool:
        """
        Informa se a pilha de estados deve ser esvaziada antes de
        adicionar os novos estados.
        """
        pass

