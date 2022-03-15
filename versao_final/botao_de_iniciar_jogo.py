import os.path
import pygame
from item_de_menu import ItemDeMenu
from item_de_menu_clicavel import ItemDeMenuClicavel
from mensagem_de_iniciar_jogo_principal import (
        MensagemDeIniciarJogoPrincipal)

class BotaoDeIniciarJogo(ItemDeMenu, ItemDeMenuClicavel):
    def __init__(self):
        self.__caminho_da_imagem = os.path.join(
                "imagens",
                "botao_de_iniciar_jogo.png"
                )
        self.__largura = 150
        self.__altura = 75
        # Posições do ponto central do botão:
        self.__posicao_x = 320 - self.__largura/2
        self.__posicao_y = 400 - self.__altura/2
        self.__area_da_superficie = pygame.Rect(
                self.__posicao_x,
                self.__posicao_y,
                self.__largura,
                self.__altura
                )
        imagem_bruta = pygame.image.load(self.__caminho_da_imagem)
        self.__superficie = imagem_bruta.convert()
        self.__mensagem_de_iniciar_jogo_principal = \
                MensagemDeIniciarJogoPrincipal()
        self.__tem_item_visivel = True

    def desenhar(self, superficie_de_desenho):
        superficie_de_desenho.blit(
                self.__superficie,
                self.__area_da_superficie
                )

    def gerenciar_clique(self) -> MensagemDeIniciarJogoPrincipal:
        return self.__mensagem_de_iniciar_jogo_principal

    @property
    def area_da_superficie(self) -> pygame.Rect:
        return self.__area_da_superficie

    @property
    def tem_item_visivel(self) -> bool:
        return self.__tem_item_visivel

