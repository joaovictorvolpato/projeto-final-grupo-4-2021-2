from renderer import Renderer
from game_state import Game_state

class RendererMenuPrincipal(Renderer):
    """
    Componente responsável por desenhar o menu principal na tela.
    """
    def __init__(self):
        self.__game_state = Game_state()

    def render(self):
        """
        Desenha os itens do menu principal na tela.
        """
        self.__desenhar_itens_comuns()
        self.__desenhar_itens_clicaveis()

    def __desenhar_itens_comuns(self):
        """
        Desenha os itens comuns do menu principal na tela.
        """
        tela = self.__game_state.win
        for item in self.__game_state.itens_de_menu_comuns:
            item.desenhar(tela)

    def __desenhar_itens_clicaveis(self):
        """
        Desenha os itens clicáveis do menu principal na tela.
        """
        tela = self.__game_state.win
        for item in self.__game_state.itens_de_menu_clicaveis:
            item.desenhar(tela)

