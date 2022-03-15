from abc_singleton import Singleton

class Game_state(metaclass=Singleton):
    """
    Armazena os dados com os quais cada estado do programa trabalha.
    """
    def __init__(self):
        self.__player = None
        self.__objects = []
        self.__kinetic_objects = []
        self.__command_objects = []
        self.__obstacles = []
        self.__event_objects = []
        self.__interactables = []
        self.__win = None
        self.__itens_de_menu_comuns = []
        self.__itens_de_menu_clicaveis = []

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, novos_dados):
        self.__player = novos_dados

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, novos_dados):
        self.__objects = novos_dados

    @property
    def kinetic_objects(self):
        return self.__kinetic_objects

    @kinetic_objects.setter
    def kinetic_objects(self, novos_dados):
        self.__kinetic_objects = novos_dados

    @property
    def command_objects(self):
        return self.__command_objects

    @command_objects.setter
    def command_objects(self, novos_dados):
        self.__command_objects = novos_dados

    @property
    def obstacles(self):
        return self.__obstacles

    @obstacles.setter
    def obstacles(self, novos_dados):
        self.__obstacles = novos_dados

    @property
    def event_objects(self):
        return self.__event_objects

    @event_objects.setter
    def event_objects(self, novos_dados):
        self.__event_objects = novos_dados

    @property
    def interactables(self):
        return self.__interactables

    @interactables.setter
    def interactables(self, novos_dados):
        self.__interactables = novos_dados

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, novos_dados):
        self.__win = novos_dados

    @property
    def itens_de_menu_comuns(self):
        return self.__itens_de_menu_comuns

    @itens_de_menu_comuns.setter
    def itens_de_menu_comuns(self, novos_dados):
        self.__itens_de_menu_comuns = novos_dados

    @property
    def itens_de_menu_clicaveis(self):
        return self.__itens_de_menu_clicaveis

    @itens_de_menu_clicaveis.setter
    def itens_de_menu_clicaveis(self, novos_dados):
        self.__itens_de_menu_clicaveis = novos_dados

