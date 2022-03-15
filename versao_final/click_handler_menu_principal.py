from game_state import Game_state
from event_handler import Event_handler
from mensagem_de_continuar import MensagemDeContinuar
from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados
from item_de_menu import ItemDeMenu

class ClickHandlerMenuPrincipal:
    """
    Gerencia os cliques feitos no menu principal.
    """
    def __init__(self):
        self.__game_state = Game_state()
        self.__event_handler = Event_handler()
        self.__interacoes = {}
        self.__tem_clique_iniciado = False
        self.__mensagem_de_continuar = MensagemDeContinuar()

    def handle(self) -> MensagemDePilhaDeEstados:
        """
        Encontra o item clicado, faz as ações apropriadas e retorna a
        mensagem para o gerenciador de estados.
        """
        self.__event_handler.key_checker()
        self.__interacoes = self.__event_handler.output

        tem_clique_valido = ((not self.__tem_clique_completado())
                or (not self.__tem_clique_intencional()))
        if not tem_clique_valido:
            return self.__mensagem_de_continuar

        posicao_do_clique = self.__interacoes['mousebuttondown_pos']
        item_clicado = self.__encontrar_item_clicado(posicao_do_clique)

        tem_item_clicado = item_clicado != None
        if not tem_item_clicado:
            return self.__mensagem_de_continuar

        mensagem = item_clicado.gerenciar_clique()

        return mensagem

    def __tem_clique_completado(self) -> bool:
        """
        Informa se o botão do mouse foi solto após ser pressionado.
        """
        tem_clique_completado = (self.__interacoes['mousebuttonup']
                and self.__tem_clique_iniciado)

        if tem_clique_completado:
            self.__tem_clique_iniciado = False
        else:
            self.__tem_clique_iniciado = (
                    self.__interacoes['mousebuttondown']
                    or self.__tem_clique_iniciado)

        return tem_clique_completado

    def __tem_clique_intencional(self) -> bool:
        """
        Informa se a posição do ponteiro do mouse no início do clique é
        igual à posição no final do clique.
        """
        posicao_do_clique_inicial = self.__interacoes['mousebuttondown_pos']
        posicao_do_clique_final = self.__interacoes['mousebuttonup_pos']
        tem_clique_intencional = \
                posicao_do_clique_inicial == posicao_do_clique_final
        return tem_clique_intencional

    def __encontrar_item_clicado(self, posicao_do_clique):
        """
        Procura pelo item, entre os itens clicáveis desenhados na tela,
        cuha área cobre o ponto do clique e retorna esse item se ele
        existir.
        """
        itens_clicaveis = self.__game_state.itens_de_menu_clicaveis

        for item in itens_clicaveis:
            tem_item_visivel = item.tem_item_visivel
            tem_clique_no_item = \
                    item.area_da_superficie.collidepoint(posicao_do_clique)
            if tem_item_visivel and tem_clique_no_item:
                return item

        return None

