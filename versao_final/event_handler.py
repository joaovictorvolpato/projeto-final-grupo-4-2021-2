import pygame


# Transforma inputs em comandos para o jogo
class Event_handler:
    def __init__(self):
        # teclas que fazem coisas no jogo, USAR PARA TIRAR IFS DPS
        self.__event_list = {'quit': pygame.QUIT, 'down': pygame.K_DOWN, 'right': pygame.K_RIGHT,
                             'left': pygame.K_LEFT, 'up': pygame.K_UP, 'space_bar': pygame.K_SPACE}
        # output desss teclas
        self.__output = {'up': False, 'down': False,
                         'right': False, 'left': False, 'quit': False, 'space_bar': False}

    # getters
    @property
    def output(self):
        return self.__output

    # cuida de novos eventos, modificando os outputs
    def key_checker(self):
        for event in pygame.event.get():
            if event.type == self.__event_list['quit']:
                self.__output['quit'] = True

            if event.type == pygame.KEYDOWN:
                for command, key in self.__event_list.items():
                    if event.key == key:
                        self.__output[command] = True

            if event.type == pygame.KEYUP:
                for command, key in self.__event_list.items():
                    if event.key == key:
                        self.__output[command] = False
