"""
Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 100, inicialmente, e o usuário tem 5 tentativas para adivinhar o número
OBS.: O design da tela pode ser implementado livremente

Forneça dica se um número informado está no intervalo maior ou menor.

Dica: Use a import random

Implemente um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, receberá a pontuação máxima (ex. 100 pontos); se o usuário adivinhar o número na última tentativa, receberá a pontuação mínima (ex. 10 pontos); se o usuário não acertar o número, não receberá nenhum ponto.

Implemente um controle de erros. Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, o sistema deve notificar o jogador e solicitar o input correto.

Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.
"""
# Bibliotecas
import random
import os


class JogoAdivinhacao:
    def __init__(self):
        self.__PONTUACAO_MAXIMA = 0
        self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR = (0, 0)
        self.__QUANTIDADE_DE_TENTATIVAS_DO_USUARIO = 0
        self.__TABELA_DE_PONTUACAO = {}

        self.__pontuacao_do_usuario = 0
        self.__lista_com_os_numeros_utilizados_pelo_usuario = []
        self.__dicionario_com_as_dicas = {}
        self.__numero_do_computador = 0

    # Set
    def definir_pontuacao_maxima(self, PONTUACAO_MAXIMA):
        self.__PONTUACAO_MAXIMA = PONTUACAO_MAXIMA


    def definir_range_de_escolha_do_computador(self, RANGE_DE_ESCOLHA_DO_COMPUTADOR):
        self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR = RANGE_DE_ESCOLHA_DO_COMPUTADOR


    def definir_quantidade_de_tentativas_do_usuario(self, QUANTIDADE_DE_TENTATIVAS_DO_USUARIO):
        self.__QUANTIDADE_DE_TENTATIVAS_DO_USUARIO = QUANTIDADE_DE_TENTATIVAS_DO_USUARIO


    def definir_tabela_de_pontuacao(self):
        for tentativa in range(self.__QUANTIDADE_DE_TENTATIVAS_DO_USUARIO):
            self.__TABELA_DE_PONTUACAO[str(tentativa + 1)] = self.__PONTUACAO_MAXIMA - self.__PONTUACAO_MAXIMA / self.__QUANTIDADE_DE_TENTATIVAS_DO_USUARIO * tentativa
    
    
    def __definir_numero_do_computador(self):
        return random.randint(self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[0], self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[1])

    
    # Get
    def obter_pontuacao_maxima(self):
        return self.__PONTUACAO_MAXIMA


    def obter_range_de_escolha_do_computador(self):
        return self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR


    def obter_quantidade_de_tentativas_do_usuario(self):
        return self.__QUANTIDADE_DE_TENTATIVAS_DO_USUARIO


    def obter_tabela_de_pontuacao(self):
        return self.__TABELA_DE_PONTUACAO


    # Funções estéticas
    def __limpar_terminal(self):
        os.system('cls||clear')


    def __mensagem_de_aviso(self, mensagem):
        print(f'[ ! ] {mensagem}')


    def __mensagem_enter_para_continuar(self):
        input('[ - ] Pressione "Enter" para continuar...')


    def __imprimir_menu_principal(self):
        print('[ - ] Menu "Configurações do Jogo"\n' +
        '[ A ] Para recomeçar o jogo\n' +
        '[ B ] Para fechar o jogo\n' +
        '\n' +
        '[ - ] Menu "Jogo da Adivinhação"\n' +
        f'[ ! ] O computador escolheu um número entre {self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[0]} e {self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[1]}\n' +
        f'\n[ - ] Pontuação: {self.__pontuacao_do_usuario} pontos\n' +
        '\n[ + ] Dicas:')
        for dica in self.__dicionario_com_as_dicas.items():
            print(f'[ - ] {int(dica[0])}ª dica | {dica[1]}')
        print('')


    def __imprimir_menu_sair_do_jogo(self):
        print('[ - ] Menu "Sair do Jogo"\n' +
        '[ ! ] Ao sair do jogo sua pontuação será perdida\n' +
        f'[ - ] Pontuação atual: {self.__pontuacao_do_usuario} pontos\n' +
        '\n' +
        '[ ? ] Tem certeza que deseja sair?\n' +
        '[ 1 ] Sim\n' + 
        '[ 2 ] Não\n')
    

    def __imprimir_menu_reiniciar_o_jogo(self):
        print('[ - ] Menu "Reiniciar o Jogo"\n' +
        '[ ! ] Ao reiniciar o jogo sua pontuação será perdida\n' +
        f'[ - ] Pontuação atual: {self.__pontuacao_do_usuario} pontos\n' +
        '\n' +
        '[ ? ] Tem certeza que deseja reiniciar?\n' +
        '[ 1 ] Sim\n' + 
        '[ 2 ] Não\n')


    # Opções do menu
    def __reiniciar_jogo(self):
        self.__pontuacao_do_usuario = 0
        self.__lista_com_os_numeros_utilizados_pelo_usuario = []
        self.__dicionario_com_as_dicas = {}
        self.__numero_do_computador = 0


    def __opcoes_do_menu_sair_do_jogo(self):
        while True:
            self.__limpar_terminal()
            self.__imprimir_menu_sair_do_jogo()
            escolha_do_usuario_no_menu_sair_do_jogo = input('[ > ] ').strip().upper()

            if escolha_do_usuario_no_menu_sair_do_jogo == '1':
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Saindo do jogo.')
                self.__mensagem_enter_para_continuar()
                self.__limpar_terminal()
                exit()
            elif escolha_do_usuario_no_menu_sair_do_jogo == '2':
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Ação de sair do jogo cancelada.')
                self.__mensagem_enter_para_continuar()
                break
            else:
                self.__limpar_terminal()
                self.__mensagem_de_aviso(f'O valor "{escolha_do_usuario_no_menu_sair_do_jogo}" não pertence as opções apresentadas no menu, tente novamente.')
                self.__mensagem_enter_para_continuar()
                

    def __opcoes_do_menu_reiniciar_o_jogo(self):
        while True:
            self.__limpar_terminal()
            self.__imprimir_menu_reiniciar_o_jogo()
            escolha_do_usuario_no_menu_reiniciar_o_jogo = input('[ > ] ').strip().upper()

            if escolha_do_usuario_no_menu_reiniciar_o_jogo == '1':
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Reiniciando o jogo.')
                self.__mensagem_enter_para_continuar()
                self.__limpar_terminal()
                self.__reiniciar_jogo()
                break
            elif escolha_do_usuario_no_menu_reiniciar_o_jogo == '2':
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Ação de reiniciar o jogo cancelada.')
                self.__mensagem_enter_para_continuar()
                break
            else:
                self.__limpar_terminal()
                self.__mensagem_de_aviso(f'O valor "{escolha_do_usuario_no_menu_reiniciar_o_jogo}" não pertence as opções apresentadas no menu, tente novamente.')
                self.__mensagem_enter_para_continuar()
                

    # Validações
    def __validar_numero_do_usuario(self, numero_do_usuario):
        try:
            numero_do_usuario = int(numero_do_usuario)

            if self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[0] <= numero_do_usuario <= self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[1] and numero_do_usuario not in self.__lista_com_os_numeros_utilizados_pelo_usuario:
                return True
            else:
                return False
        except:
            return False


    def __verificar_se_o_usuario_acertou(self, numero_usuario):
        if numero_usuario == self.__numero_do_computador:
            return True
        else:
            return False


    def __verificar_se_numero_do_usuario_e_maior_ou_menor(self, numero_usuario):
        if numero_usuario > self.__numero_do_computador:
            return 'maior'
        else:
            return 'menor'


    # Função Main
    def iniciar_jogo(self):
        while True:
            usuario_acertou_o_numero_do_computador = False
            self.__numero_do_computador = self.__definir_numero_do_computador()
            for rodada_atual in range(self.__QUANTIDADE_DE_TENTATIVAS_DO_USUARIO):
                while True:
                    self.__limpar_terminal()
                    self.__imprimir_menu_principal()
                    escolha_do_usuario_no_menu_principal = input('[ > ] ').strip().upper()

                    if escolha_do_usuario_no_menu_principal == 'A':
                        self.__opcoes_do_menu_reiniciar_o_jogo()
                    elif escolha_do_usuario_no_menu_principal == 'B':
                        self.__opcoes_do_menu_sair_do_jogo()
                    else:
                        if self.__validar_numero_do_usuario(escolha_do_usuario_no_menu_principal):
                            escolha_do_usuario_no_menu_principal = int(escolha_do_usuario_no_menu_principal)
                            break
                        else:
                            self.__limpar_terminal()
                            self.__mensagem_de_aviso(f'O valor "{escolha_do_usuario_no_menu_principal}" é inválido ou está fora do range ({self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[0]} - {self.__RANGE_DE_ESCOLHA_DO_COMPUTADOR[1]})')
                            self.__mensagem_enter_para_continuar()
                
                # Verificar status
                if self.__verificar_se_o_usuario_acertou(escolha_do_usuario_no_menu_principal):
                    self.__limpar_terminal()
                    self.__pontuacao_do_usuario += self.__TABELA_DE_PONTUACAO[str(rodada_atual + 1)]

                    print(f'[ - ] Você acertou e ganhou {self.__TABELA_DE_PONTUACAO[str(rodada_atual + 1)]} pontos.\n' +
                    f'[ - ] Pontuação atual: {self.__pontuacao_do_usuario} pontos.\n')
                    self.__mensagem_enter_para_continuar()
                    
                    usuario_acertou_o_numero_do_computador = True
                    break
                else:
                    self.__limpar_terminal()
                    self.__mensagem_de_aviso(f'O número "{escolha_do_usuario_no_menu_principal}" é {self.__verificar_se_numero_do_usuario_e_maior_ou_menor(escolha_do_usuario_no_menu_principal)} que o número do computador.')
                    self.__mensagem_enter_para_continuar()
                    
                    self.__dicionario_com_as_dicas[str(rodada_atual + 1)] = f'O número "{escolha_do_usuario_no_menu_principal}" é {self.__verificar_se_numero_do_usuario_e_maior_ou_menor(escolha_do_usuario_no_menu_principal)} que o número do computador.'
                    self.__lista_com_os_numeros_utilizados_pelo_usuario.append(int(escolha_do_usuario_no_menu_principal))
            
            if not usuario_acertou_o_numero_do_computador:
                self.__limpar_terminal()
                self.__mensagem_de_aviso('Suas tentativas acabaram.')
                print(f'[ - ] O número do computador era "{self.__numero_do_computador}".\n[ - ] Boa sorte na próxima.\n')
                self.__mensagem_enter_para_continuar()
            self.__lista_com_os_numeros_utilizados_pelo_usuario = []
            self.__dicionario_com_as_dicas = {}
