import os
import random

class JogoDaForca:
    def __init__(self, BANCO_DE_PALAVRAS):
        self.__lista_de_letras_digitadas_pelo_usuario = []
        self.__erros_do_usuario = 0

        self.__QUANTIDADE_DE_ERROS = 6
        self.__PALAVRA_SECRETA = ''
        self.__palavra_secreta_display = []

        self.__BANCO_DE_PALAVRAS = BANCO_DE_PALAVRAS
        self.__PALAVRA_SECRETA = self.__gerar_palavra_secreta().upper()
        self.__palavra_secreta_display = ['_'] * len(self.__PALAVRA_SECRETA)

        
    def __gerar_palavra_secreta(self):
        with open(str(f"{self.__BANCO_DE_PALAVRAS}"), 'r', encoding = 'utf-8') as banco_de_palavras:
            return random.choice(banco_de_palavras.readlines()[0].split(' '))

        
    def __conferir_se_a_letra_esta_na_palavra_secreta(self, letra_digitada_pelo_usuario):
        if letra_digitada_pelo_usuario in self.__PALAVRA_SECRETA:
            return True
        else:
            return False


    def __conferir_se_a_letra_ja_foi_digitada(self, letra_digitada_pelo_usuario):
        if letra_digitada_pelo_usuario in self.__lista_de_letras_digitadas_pelo_usuario:
            return True
        else:
            return False


    @staticmethod
    def __imprimir_menu_principal():
        print('[ - ] Menu principal "Jogo da forca"\n' + 
        '[ 1 ] Iniciar jogo\n' +
        '[ 2 ] Sair do jogo\n')


    @staticmethod
    def __imprimir_menu_sair_do_jogo():
        print('[ - ] Menu "Sair do Jogo"\n' +
        '[ ! ] Ao sair todo o seu progresso será perdido\n' +
        '\n' +
        '[ ? ] Tem certeza que deseja sair?\n' +
        '[ 1 ] Sim\n' + 
        '[ 2 ] Não\n')


    def __menu_iniciando_jogo(self):
        self.__imprimir_situacao_do_jogo()
        print('\n[ - ] Palavra secreta | ', end=''); self.__imprimir_a_palavra_secreta()
        print()
        print('[ - ] Letras que você já tentou | ', end=''); [print(f'{letra} ', end='') if index != (len(self.__lista_de_letras_digitadas_pelo_usuario) - 1) else print(letra) for index, letra in enumerate(sorted(self.__lista_de_letras_digitadas_pelo_usuario))] if len(self.__lista_de_letras_digitadas_pelo_usuario) > 0 else print()
        print(f'[ - ] Quantidade de erros | {self.__erros_do_usuario}\n')


    def __atualizar_estado_atual_da_palavra_secreta(self, letra_digitada_pelo_usuario):
        self.__palavra_secreta_display[self.__PALAVRA_SECRETA.find(letra_digitada_pelo_usuario)] = letra_digitada_pelo_usuario
        index_proprio = self.__PALAVRA_SECRETA.find(letra_digitada_pelo_usuario)
        for _ in range(self.__PALAVRA_SECRETA.count(letra_digitada_pelo_usuario) - 1):
            self.__palavra_secreta_display[self.__PALAVRA_SECRETA.find(letra_digitada_pelo_usuario, index_proprio)] = letra_digitada_pelo_usuario
            index_proprio = self.__PALAVRA_SECRETA.find(letra_digitada_pelo_usuario, index_proprio + 1)
        self.__palavra_secreta_display[self.__PALAVRA_SECRETA.find(letra_digitada_pelo_usuario, index_proprio)] = letra_digitada_pelo_usuario


    def __imprimir_a_palavra_secreta(self):
        for index, letra in enumerate(self.__palavra_secreta_display):
            print(f'{letra} ', end='') if not index == len(self.__palavra_secreta_display) - 1 else print(f'{letra}', end='')


    def __opcoes_do_menu_sair_do_jogo(self):
        while True:
            self.__limpar_terminal()
            self.__imprimir_menu_sair_do_jogo()
            escolha_do_usuario_no_menu_sair_do_jogo = input('[ > ] ').strip().upper()

            if escolha_do_usuario_no_menu_sair_do_jogo == '1':
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Saindo do jogo.')
                print()
                self.__mensagem_enter_para_continuar()
                self.__limpar_terminal()
                exit()
            elif escolha_do_usuario_no_menu_sair_do_jogo == '2':
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Ação de sair do jogo cancelada.')
                print()
                self.__mensagem_enter_para_continuar()
                break
            else:
                self.__limpar_terminal()
                self.__mensagem_de_aviso(f'O valor "{escolha_do_usuario_no_menu_sair_do_jogo}" não pertence as opções apresentadas no menu, tente novamente.')
                print()
                self.__mensagem_enter_para_continuar()


    def __imprimir_situacao_do_jogo(self):
        desenho_inicial = [
            [' ', ' ', '_', '_', '_', '_', '_', ' ', ' '],
            [' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-']
        ]

        local_para_desenhar = {
            1 : "desenho_inicial[2][1] = 'O'",
            2 : "desenho_inicial[3][1] = '|'",
            3 : "desenho_inicial[3][0] = '/'",
            4 : r"desenho_inicial[3][2] = '\\'",
            5 : "desenho_inicial[4][0] = '/'",
            6 : r"desenho_inicial[4][2] = '\\'"
        }

        for erro in range(self.__erros_do_usuario):
            exec(local_para_desenhar[erro + 1])

        for linha_para_desenhar in desenho_inicial:
            for caracter_para_desenhar in linha_para_desenhar:
                print(caracter_para_desenhar, end='')
            print()


    @staticmethod
    def __validar_letra_digitada_pelo_usuario(letra_digitada_pelo_usuario):
        if letra_digitada_pelo_usuario != '\n' and letra_digitada_pelo_usuario.isalpha() and len(letra_digitada_pelo_usuario) == 1 or letra_digitada_pelo_usuario == '-':
            return True
        else:
            return False


    def __iniciando_jogo(self):
        usuario_acertou_a_palavra = False
        for rodada_atual in range(self.__QUANTIDADE_DE_ERROS):
            while True:
                self.__limpar_terminal()
                self.__menu_iniciando_jogo()
                letra_digitada_pelo_usuario = input('[ > ] ').strip().upper()

                if self.__validar_letra_digitada_pelo_usuario(letra_digitada_pelo_usuario):
                    if not self.__conferir_se_a_letra_ja_foi_digitada(letra_digitada_pelo_usuario):
                        self.__lista_de_letras_digitadas_pelo_usuario.append(letra_digitada_pelo_usuario)

                        if self.__conferir_se_a_letra_esta_na_palavra_secreta(letra_digitada_pelo_usuario):
                            self.__limpar_terminal()
                            self.__mensagem_de_aviso(f'Você acertou a letra "{letra_digitada_pelo_usuario}".')
                            print()
                            self.__mensagem_enter_para_continuar()
                            self.__atualizar_estado_atual_da_palavra_secreta(letra_digitada_pelo_usuario)
                        else:
                            self.__limpar_terminal()
                            self.__mensagem_de_aviso(f'A letra "{letra_digitada_pelo_usuario}" não pertence a palavra secreta.')
                            print()
                            self.__mensagem_enter_para_continuar()
                            self.__erros_do_usuario += 1
                            break

                        if self.__palavra_secreta_display.count('_') == 0:
                                self.__limpar_terminal()
                                self.__mensagem_de_aviso(f'Você acertou, a palavra era "{self.__PALAVRA_SECRETA}".')
                                print()
                                self.__mensagem_enter_para_continuar()
                                usuario_acertou_a_palavra = True
                                break
                    else:
                        self.__limpar_terminal()
                        self.__mensagem_de_aviso(f'A letra "{letra_digitada_pelo_usuario}" já foi digitada.')
                        print()
                        self.__mensagem_enter_para_continuar()
                else:
                    self.__limpar_terminal()
                    self.__mensagem_de_aviso(f'O valor "{letra_digitada_pelo_usuario}" é inválido.')
                    print()
                    self.__mensagem_enter_para_continuar()
            
            if usuario_acertou_a_palavra:
                break
            else:
                if rodada_atual == 5:
                    self.__limpar_terminal()
                    self.__mensagem_de_aviso(f'Suas tentativas acabaram.')
                    self.__mensagem_de_aviso(f'A palavra secreta era "{self.__PALAVRA_SECRETA}".')
                    self.__mensagem_de_aviso('Boa sorte no próximo jogo.')
                    print()
                    self.__mensagem_enter_para_continuar() 
                    break


    def __reiniciar_informacoes_sobre_o_jogo(self):
        self.__PALAVRA_SECRETA = self.__gerar_palavra_secreta().upper()
        self.__palavra_secreta_display = ['_'] * len(self.__PALAVRA_SECRETA)
        self.__lista_de_letras_digitadas_pelo_usuario = []
        self.__erros_do_usuario = 0


    def iniciar_jogo(self):
        while True:
            self.__limpar_terminal()
            self.__imprimir_menu_principal()
            escolha_do_usuario_no_menu_principal = input('[ > ] ').strip()
            
            if escolha_do_usuario_no_menu_principal == '1':
                self.__iniciando_jogo()
            elif escolha_do_usuario_no_menu_principal == '2':
                self.__opcoes_do_menu_sair_do_jogo()
            else:
                self.__limpar_terminal()
                self.__mensagem_de_aviso(f'O valor "{escolha_do_usuario_no_menu_principal}" é inválido ou não pertence ao menu principal.')
                self.__mensagem_enter_para_continuar()
            
            self.__reiniciar_informacoes_sobre_o_jogo()


    @staticmethod
    def __limpar_terminal():
        os.system('cls||clear')


    @staticmethod
    def __mensagem_de_aviso(mensagem):
        print(f'[ ! ] {mensagem}')


    @staticmethod
    def __mensagem_enter_para_continuar():
        input('[ - ] Pressione "Enter" para continuar...')
