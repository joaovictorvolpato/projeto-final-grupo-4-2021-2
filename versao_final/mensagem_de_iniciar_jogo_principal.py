from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados
from jogo_principal import JogoPrincipal

class MensagemDeIniciarJogoPrincipal(MensagemDePilhaDeEstados):
    """
    Esta mensagem contém as instruções de remover os estados anteriores
    da pilha de estados do programa e de iniciar o jogo principal.
    """
    def __init__(self):
        self.__numero_de_estados_para_remover = 0
        self.__estados_para_adicionar = [JogoPrincipal()]
        self.__esvaziar_pilha_de_estados = True

    @property
    def numero_de_estados_para_remover(self):
        return self.__numero_de_estados_para_remover

    @property
    def estados_para_adicionar(self):
        return self.__estados_para_adicionar

    @property
    def esvaziar_pilha_de_estados(self):
        return self.__esvaziar_pilha_de_estados

