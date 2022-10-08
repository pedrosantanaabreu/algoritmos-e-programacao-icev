from cores import Cores
import os

class Utilitarios:
    def __init__(self, tamanho_da_interface):
        self.__COR_PADRAO_DA_INTERFACE = 'azul'
        self.__CORES_E_ESTILOS = Cores()
        self.__TAMANHO_EIXO_X_DA_TELA = (len(tamanho_da_interface) % 10) * 10 + 20
        self.__PORCENTAGEM_TAMANHO_DA_BORDA_LATERAL_DA_TELA = 10 / 100
        self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA = 1 if not int(self.__TAMANHO_EIXO_X_DA_TELA * self.__PORCENTAGEM_TAMANHO_DA_BORDA_LATERAL_DA_TELA) else int(self.__TAMANHO_EIXO_X_DA_TELA * self.__PORCENTAGEM_TAMANHO_DA_BORDA_LATERAL_DA_TELA)


    def imprimir_pagina_inicial(self, dicionario_com_as_dicas, pontuacao_do_usuario, RANGE_DE_ESCOLHA_DO_COMPUTADOR, ):
        @staticmethod
        def adicionar_linha_de_texto_personalizada(texto, codigo_do_estilo, codigo_do_texto, codigo_do_fundo):
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}')
            self.__CORES_E_ESTILOS.print_personalizado_personalizado(codigo_do_estilo = codigo_do_estilo, codigo_do_texto = codigo_do_texto, codigo_do_fundo = codigo_do_fundo, texto = f'{texto.center(self.__TAMANHO_EIXO_X_DA_TELA - self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA * 2)}')
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}\n')

    
        @staticmethod
        def adicionar_linha_de_texto(texto):
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}')
            print(f'{texto.center(self.__TAMANHO_EIXO_X_DA_TELA - self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA * 2)}', end='')
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}\n')


        @staticmethod
        def adicionar_linha_vazia():
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}')
            print(f'{" " * (self.__TAMANHO_EIXO_X_DA_TELA - self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA * 2)}', end='')
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}\n')


        @staticmethod
        def adicionar_linha_completa():
            self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHO_EIXO_X_DA_TELA}\n')


        @staticmethod
        def exibir_dicas():
            for dica in dicionario_com_as_dicas.items():
                adicionar_linha_de_texto(f'{int(dica[0])}ª dica | {dica[1]}')

        # Titulos e informações da tela
        titulo_da_pagina_incial = '¿ Jogo Adivinhe ?'
        titulo_do_autor = 'feito por @pedrosantanaabreu'

        titulo_do_menu_inicial = 'Menu Inicial'
        subtitulo_1_do_menu_inicial = '[ A ] Para reiniciar o jogo'
        subtitulo_2_do_menu_inicial = '[ B ] Para finalizar o jogo'

        titulo_do_menu_do_jogo = 'Menu do Jogo'
        subtitulo_1_do_menu_do_jogo = f'Digite um número entre {RANGE_DE_ESCOLHA_DO_COMPUTADOR[0]} e {RANGE_DE_ESCOLHA_DO_COMPUTADOR[1]}'
        subtitulo_2_do_menu_do_jogo = f'Pontuação atual | {pontuacao_do_usuario} pontos'
        subtitulo_3_do_menu_do_jogo = 'Dicas'

        # Parte introdução
        adicionar_linha_completa()
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(titulo_da_pagina_incial, codigo_do_estilo = 0, codigo_do_texto = 1, codigo_do_fundo = 1)
        adicionar_linha_de_texto(titulo_do_autor)
        adicionar_linha_vazia()
        adicionar_linha_completa()
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(titulo_do_menu_inicial, codigo_do_estilo = 0, codigo_do_texto = 1, codigo_do_fundo = 1)
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(subtitulo_1_do_menu_inicial, codigo_do_estilo = 1, codigo_do_texto = 34, codigo_do_fundo = 40)
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(subtitulo_2_do_menu_inicial, codigo_do_estilo = 1, codigo_do_texto = 31, codigo_do_fundo = 40)
        adicionar_linha_vazia()
        adicionar_linha_completa()
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(titulo_do_menu_do_jogo, codigo_do_estilo = 0, codigo_do_texto = 1, codigo_do_fundo = 1)
        adicionar_linha_vazia()
        adicionar_linha_de_texto(subtitulo_1_do_menu_do_jogo)
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(subtitulo_2_do_menu_do_jogo, codigo_do_estilo = 1, codigo_do_texto = 33, codigo_do_fundo = 40)
        adicionar_linha_vazia()
        adicionar_linha_de_texto_personalizada(subtitulo_3_do_menu_do_jogo, codigo_do_estilo = 1, codigo_do_texto = 32, codigo_do_fundo = 40)
        exibir_dicas()
        adicionar_linha_vazia()
        adicionar_linha_completa()
        self.__CORES_E_ESTILOS.print_personalizado(cor_de_fundo = self.__COR_PADRAO_DA_INTERFACE, texto = f'{" " * self.__TAMANHDO_DA_BORDA_LATERAL_DA_TELA}')


    @staticmethod
    def __limpar_terminal():
        os.system('cls||clear')


    @staticmethod
    def __mensagem_de_aviso(mensagem):
        print(f'[ ! ] {mensagem}')


    @staticmethod
    def __mensagem_enter_para_continuar():
        input('[ - ] Pressione "Enter" para continuar...')
