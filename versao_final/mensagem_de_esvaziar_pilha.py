from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados

class MensagemDeEsvaziarPilha(MensagemDePilhaDeEstados):
    """
    Esta mensagem contém a instrução de remover todos os estados da
    pilha de estados.
    """
    def __init__(self):
        self.__numero_de_estados_para_remover = 0
        self.__estados_para_adicionar = []
        self.__esvaziar_pilha_de_estados = True

    @property
    def numero_de_estados_para_remover(self) -> int:
        return self.__numero_de_estados_para_remover

    @property
    def estados_para_adicionar(self) -> list:
        return self.__estados_para_adicionar

    @property
    def esvaziar_pilha_de_estados(self) -> bool:
        return self.__esvaziar_pilha_de_estados

