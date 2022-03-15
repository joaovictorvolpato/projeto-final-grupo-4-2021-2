import os.path
import pygame
from item_de_menu import ItemDeMenu

class FundoDoMenuPrincipal(ItemDeMenu):
    def __init__(self):
        self.__caminho_da_imagem = os.path.join(
                "imagens",
                "fundo_do_menu_principal.png"
                )
        self.__posicao_x = 0
        self.__posicao_y = 0
        self.__largura = 600
        self.__altura = 600
        self.__area_da_superficie = pygame.Rect(
                self.__posicao_x,
                self.__posicao_y,
                self.__largura,
                self.__altura
                )
        imagem_bruta = pygame.image.load(self.__caminho_da_imagem)
        self.__superficie = imagem_bruta.convert()
        self.__tem_item_visivel = True

    def desenhar(self, superficie_de_desenho):
        superficie_de_desenho.blit(
                self.__superficie,
                self.__area_da_superficie
                )

    @property
    def area_da_superficie(self) -> pygame.Rect:
        return self.__area_da_superficie

    @property
    def tem_item_visivel(self) -> bool:
        return self.__tem_item_visivel

