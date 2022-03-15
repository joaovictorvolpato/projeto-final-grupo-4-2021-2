from menu_principal import MenuPrincipal
from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados
from pygame import quit as pygame_quit
from sys import exit as sys_exit

class GerenciadorDeEstados:
    """
    Gerencia o sistema de estados baseado em uma pilha, ou "stack", e a
    transferência de estados.
    """
    def __init__(self):
        estado_inicial = MenuPrincipal()
        self.__estados = [estado_inicial]

    def processar(self):
        """
        Realiza a rotina do estado atual e atualiza a pilha de estados
        com as informações recebidas.
        """
        try:
            estado_atual = self.__estados[-1]
            mensagem = estado_atual.execute_game_routine()
            self.__atualizar_pilha_de_estados(mensagem)
        except IndexError:
            self.__fechar_programa()

    def __atualizar_pilha_de_estados(
            self,
            mensagem: MensagemDePilhaDeEstados):
        """
        Atualiza a pilha de estados com base na mensagem retornada pelo
        estado atual.
        """
        if mensagem.esvaziar_pilha_de_estados:
            numero_de_estados_para_remover = len(self.__estados)
        else:
            numero_de_estados_para_remover = \
                    mensagem.numero_de_estados_para_remover

        self.__remover_estados(numero_de_estados_para_remover)

        estados_para_adicionar = mensagem.estados_para_adicionar
        self.__adicionar_estados(estados_para_adicionar)

    def __adicionar_estados(self, estados: list):
        """
        Adiciona novos estados ao fim da lista.
        """
        self.__estados.extend(estados)

    def __remover_estados(self, numero_de_estados: int):
        """
        Remove um número de estados do fim da lista.
        """
        indice_final = len(self.__estados)
        indice_inicial = indice_final - numero_de_estados
        estados_para_remover = self.__estados[indice_inicial:indice_final]
        for estado in estados_para_remover:
            estado.limpar()
        del self.__estados[indice_inicial:indice_final]

    def __fechar_programa(self):
        """
        Fecha o programa.
        """
        pygame_quit()
        sys_exit()

