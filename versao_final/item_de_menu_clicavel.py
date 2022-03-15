from abc import ABC, abstractmethod
from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados

class ItemDeMenuClicavel(ABC):
    """
    Esta classe funciona como uma interface que deve ser apresentada,
    em conjunto com outras interfaces, por itens de menu que podem ser
    clicados.
    """
    @abstractmethod
    def gerenciar_clique(self) -> MensagemDePilhaDeEstados:
        """
        Retorna uma mensagem que informa para qual estado o programa
        deverá ir.
        """
        pass

