from carregador_de_dados import CarregadorDeDados
from game_state import Game_state
from fundo_do_menu_principal import FundoDoMenuPrincipal
from botao_de_iniciar_jogo import BotaoDeIniciarJogo
from botao_de_sair import BotaoDeSair

class CarregadorDeDadosDoMenuPrincipal(CarregadorDeDados):
    """
    Componente responsável por carregar os dados com os quais o menu
    principal trabalha no estado de jogo.
    """
    def __init__(self):
        self.__game_state = Game_state()

    def carregar(self):
        """
        Carrega os dados do menu principal no estado de jogo.
        """
        self.__game_state.itens_de_menu_comuns = [
                FundoDoMenuPrincipal()
                ]
        self.__game_state.itens_de_menu_clicaveis = [
                BotaoDeIniciarJogo(),
                BotaoDeSair()
                ]

    def limpar(self):
        """
        Limpa os dados do menu principal do estado de jogo.
        """
        self.__game_state.itens_de_menu_comuns = []
        self.__game_state.itens_de_menu_clicaveis = []

