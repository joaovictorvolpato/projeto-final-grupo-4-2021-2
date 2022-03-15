from carregador_de_dados import CarregadorDeDados
from game_state import Game_state
from tile_map import Tile_map_constructor

class CarregadorDeDadosDoJogoPrincipal(CarregadorDeDados):
    """
    Componente responsável por carregar os dados com os quais o jogo
    principal trabalha no estado de jogo.
    """
    def __init__(self):
        self.__game_state = Game_state()

    def carregar(self, level: int):
        """
        Carrega os dados do nível recebido como argumento no estado de
        jogo.
        """
        tile_map = Tile_map_constructor(level)
        self.__game_state.tile_map = tile_map
        self.__game_state.obstacles = tile_map.obstacle_list
        self.__game_state.player = tile_map.player
        self.__game_state.interactables = tile_map.interactable_list
        self.__game_state.objects = tile_map.object_list
        self.__game_state.kinetic_objects = tile_map.kinetic_list
        self.__game_state.command_objects = tile_map.command_list
        self.__game_state.event_objects = tile_map.event_list

    def limpar(self):
        """
        Limpa os dados do jogo principal do estado de jogo.
        """
        self.__game_state.tile_map = None
        self.__game_state.obstacles = []
        self.__game_state.player = None
        self.__game_state.interactables = []
        self.__game_state.objects = []
        self.__game_state.kinetic_objects = []
        self.__game_state.command_objects = []
        self.__game_state.event_objects = []

