from abc import ABC, abstractmethod
from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados

class EstadoDeJogo(ABC):
    """
    Esta classe funciona como uma interface que os estados do programa
    apresentam.
    """
    @abstractmethod
    def execute_game_routine(self) -> MensagemDePilhaDeEstados:
        """
        Faz as ações do estado do programa.
        """
        pass

    @abstractmethod
    def limpar(self):
        """
        Limpa os dados com os quais o estado trabalha.
        """
        pass

