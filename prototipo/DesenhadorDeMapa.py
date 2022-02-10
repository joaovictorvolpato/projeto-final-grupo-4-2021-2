from math import floor
from config import altura_do_bloco, largura_do_bloco, caminhos_das_imagens_dos_blocos

class DesenhadorDeMapa:
    def __init__(self, dados_do_terreno):
        self.__dados_do_terreno = dados_do_terreno

        self.__numero_de_blocos_verticais_do_mapa = \
                len(self.__dados_do_terreno)

        self.__numero_de_blocos_horizontais_do_mapa = \
                len(self.__dados_do_terreno[0])

        self.__superficies_dos_blocos = \
                self.__converter_caminhos_em_blocos(
                        caminhos_das_imagens_dos_blocos
                        )

    def __converter_caminhos_em_blocos(self, caminhos_das_imagens):
        """
        Retorna as superfícies do tipo pygame.Surface a partir dos caminhos
        das imagens dos blocos.
        """
        superficies = (pygame.image.load(imagem).convert() \
                for imagem in caminhos_das_imagens)
        
        return superficies

    def desenhar(self, janela, coordenadas_do_personagem):
        """
        Desenha o terreno do mapa do nível atual na janela a partir das
        coordenadas do personagem principal.
        """
        
        deslocamentos_dos_blocos = \
                self.__obter_deslocamentos_dos_blocos(
                        coordenadas_do_personagem
                        )

        intervalo_x, intervalo_y = \
                self.__obter_intervalos_de_blocos_proximos(
                        coordenadas_do_personagem
                        )

        inicios_dos_intervalos = (intervalo_x[0], intervalo_y[0])

        for indice_y in intervalo_y:
            for indice_x in intervalo_x:
                indices_do_bloco_para_desenhar = (indice_x, indice_y)

                superficie_do_bloco = self.__obter_superficie_do_bloco(
                        indices_do_bloco_para_desenhar
                        )

                coordenadas_do_bloco = self.__obter_coordenadas_do_bloco(
                        deslocamentos_dos_blocos,
                        indices_do_bloco_para_desenhar
                        inicios_dos_intervalos,
                        )
               
                janela.blit(superficie_do_bloco, coordenadas_do_bloco)

    def __obter_deslocamentos_dos_blocos(self, coordenadas_do_personagem):
        """
        Calcula os deslocamentos x e y que devem ser adicionados à posição
        dos blocos desenhados na tela.
        """
        posicao_x, posicao_y = coordenadas_do_personagem
        
        centro_do_bloco_x = (largura_do_bloco / 2)
        centro_do_bloco_y = (altura_do_bloco / 2)

        deslocamento_interno_ao_bloco_x = (posicao_x % altura_do_bloco)
        deslocamento_interno_ao_bloco_y = (posicao_y % largura_do_bloco)

        deslocamento_x = (
                centro_do_bloco_x
                - deslocamento_interno_ao_bloco_x
                )
        deslocamento_y = (
                centro_do_bloco_y
                - deslocamento_interno_ao_bloco_y
                )
        
        return deslocamento_x, deslocamento_y

    def __obter_intervalos_de_blocos_proximos(
            self,
            coordenadas_do_personagem
            ):
        """
        Calcula os índices dos blocos, dentro da lista de dados de terreno,
        que devem ser desenhados na tela ao redor do personagem principal.
        """
        numero_de_blocos_ao_redor_do_jogador = 5
        numero_de_blocos_adicionais_desenhados = 1

        bloco_x, bloco_y = \
                self.__obter_indices_dos_blocos_pelas_coordenadas(
                        coordenadas_do_personagem
                        )

        # Intervalo de índices horizontais, no eixo x:
        bloco_de_inicio_x = max(
                0,
                bloco_x - numero_de_blocos_ao_redor_do_jogador
                - numero_de_blocos_adicionais_desenhados
                )
        bloco_de_fim_x = min(
                self.__numero_de_blocos_horizontais_do_mapa - 1,
                bloco_x + numero_de_blocos_ao_redor_do_jogador
                + numero_de_blocos_adicionais_desenhados
                )

        # Intervalo de índices verticais, no eixo y:
        bloco_de_inicio_y = max(
                0,
                bloco_y - numero_de_blocos_ao_redor_do_jogador
                - numero_de_blocos_adicionais_desenhados
                )
        bloco_de_fim_y = min(
                self.__numero_de_blocos_verticais_do_mapa - 1,
                bloco_y + numero_de_blocos_ao_redor_do_jogador
                + numero_de_blocos_adicionais_desenhados
                )

        intervalo_x = range(
                bloco_de_inicio_x,
                bloco_de_fim_x + 1
                )
        intervalo_y = range(
                bloco_de_inicio_y,
                bloco_de_fim_y + 1
                )

        return intervalo_x, intervalo_y

    def __obter_indices_dos_blocos_pelas_coordenadas(self, coordenadas):
        """
        Calcula os índices x e y do bloco, dentro da lista de dados de
        terreno, ao qual as coordenadas x e y correspondem.
        """
        posicao_x, posicao_y = coordenadas
        indice_do_bloco_x = floor(posicao_x / largura_do_bloco)
        indice_do_bloco_y = floor(posicao_y / altura_do_bloco)
        return indice_do_bloco_x, indice_do_bloco_y

    def __obter_superficie_do_bloco(self, indices_do_bloco):
        """
        Retorna a superfície do tipo pygame.Surface a partir do número do
        tipo do bloco definido nas configurações do jogo.
        """
        indice_x, indice_y = indices_do_bloco

        numero_do_tipo_do_bloco = \
                self.__dados_do_terreno[indice_y][indice_x]
        
        superficie_do_bloco = \
                self.__superficies_dos_blocos[numero_do_tipo_do_bloco]
        
        return superficie_do_bloco

    def __obter_coordenadas_do_bloco(
            self,
            deslocamentos_dos_blocos,
            indices_do_bloco_para_desenhar,
            inicios_dos_intervalos
            ):

        deslocamento_x_do_bloco, deslocamento_y_do_bloco = \
                deslocamentos_dos_blocos

        inicio_x, inicio_y = inicios_dos_intervalos

        indice_x, indice_y = indices_do_bloco_para_desenhar
        
        indice_x_na_tela = indice_x - inicio_x
        indice_y_na_tela = indice_y - inicio_y

        coordenada_x_do_bloco = (
                indice_x_na_tela * largura_do_bloco
                + deslocamento_x_dos_blocos
                )

        coordenada_y_do_bloco = (
                indice_y_na_tela * altura_do_bloco
                + deslocamento_y_dos_blocos
                )
        
        coordenadas_do_bloco = \
                (coordenada_x_do_bloco, coordenada_y_do_bloco)

        return coordenadas_do_bloco

