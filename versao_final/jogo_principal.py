from estado_de_jogo import EstadoDeJogo
from game_state import Game_state
from renderer_jogo_principal import RendererJogoPrincipal
from command_handler import Command_handler
from movement_handler import Movement_handler
from event_object_handler import Event_object_handler
from carregador_de_dados_do_jogo_principal import (
        CarregadorDeDadosDoJogoPrincipal)
from mensagem_de_pilha_de_estados import MensagemDePilhaDeEstados
from mensagem_de_continuar import MensagemDeContinuar

class JogoPrincipal(EstadoDeJogo):
    """
    Esta classe representa o estado de jogo principal.
    """
    def __init__(self):
        self.__game_state = Game_state()
        self.__renderer = RendererJogoPrincipal()
        self.__command_handler = Command_handler()
        self.__movement_handler = Movement_handler()
        self.__carregador = CarregadorDeDadosDoJogoPrincipal()
        self.__event_object_handler = Event_object_handler(self.__carregador)
        # Mudar nivel_inicial para o nível escolhido no menu de escolha
        # de nível:
        nivel_inicial = 1
        self.__carregador.carregar(nivel_inicial)

    def execute_game_routine(self) -> MensagemDePilhaDeEstados:
        self.__renderer.render()

        self.__command_handler.execute()

        self.__movement_handler.move()

        self.__event_object_handler.handle_interactions()

        # Esta mensagem é retornada por enquanto até que a lógica de
        # transferência de estados de jogo seja completada:
        mensagem_de_continuar = MensagemDeContinuar()
        return mensagem_de_continuar

    def limpar(self):
        self.__carregador.limpar()

