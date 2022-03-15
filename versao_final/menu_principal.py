from estado_de_jogo import EstadoDeJogo
from renderer_menu_principal import RendererMenuPrincipal
from click_handler_menu_principal import ClickHandlerMenuPrincipal
from carregador_de_dados_do_menu_principal import (
        CarregadorDeDadosDoMenuPrincipal)

class MenuPrincipal(EstadoDeJogo):
    """
    Esta classe representa o estado de menu principal.
    """
    def __init__(self):
        self.__renderer = RendererMenuPrincipal()
        self.__click_handler = ClickHandlerMenuPrincipal()
        self.__carregador = CarregadorDeDadosDoMenuPrincipal()
        self.__carregador.carregar()

    def execute_game_routine(self):
        self.__renderer.render()
        mensagem = self.__click_handler.handle()
        return mensagem

    def limpar(self):
        self.__carregador.limpar()

