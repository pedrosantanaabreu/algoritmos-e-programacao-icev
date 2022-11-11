class Interfaces:
    @staticmethod
    def criar_linha(tipo: str = '', texto: str = '', ordenacao: str = '', tamanho: int = 0, borda: int = 0):
        if tipo == 'vazia':
            print(' ' * tamanho)
        elif tipo == 'branco':
            print('|' + (' ' * (tamanho - 2)) + '|')
        elif tipo == 'preenchida':
            print('+' + ('-' * (tamanho - 2)) + '+')
        elif tipo == 'ordenada':
            if  ordenacao == 'centro':
                print('|' + texto.center(tamanho - 2) + '|')
            elif ordenacao == 'esquerda':
                print('|'+ ' ' * borda + (texto.ljust(tamanho - (borda + 2))) + '|')


    @staticmethod
    def calcular_tamanho(texto):
        TAMANHO = len(texto)
        if TAMANHO < 50:
            TAMANHO = 50
        else:
            while TAMANHO % 10:
                TAMANHO += 1
            else:
                TAMANHO += 10
        return TAMANHO


    @staticmethod
    def calcular_borda(texto, tamanho):
        borda = int(tamanho / 2 - 1 - (len(texto) / 2))
        return borda


    @classmethod
    def imprimir_menu(classe, tamanho, titulo, opcoes=''):
        TAMANHO = classe.calcular_tamanho(tamanho)
        BORDA = classe.calcular_borda(titulo, TAMANHO)

        classe.criar_linha(tipo='preenchida', tamanho=TAMANHO)
        classe.criar_linha(tipo='branco', tamanho=TAMANHO)
        classe.criar_linha(tipo='ordenada', ordenacao='centro', tamanho=TAMANHO, texto=titulo)
        classe.criar_linha(tipo='branco', tamanho=TAMANHO)
        classe.criar_linha(tipo='preenchida', tamanho=TAMANHO)
        classe.criar_linha(tipo='vazia', tamanho=TAMANHO)

        if opcoes:
            classe.criar_linha(tipo='preenchida', tamanho=TAMANHO)
            classe.criar_linha(tipo='branco', tamanho=TAMANHO)
            for index, opcao in enumerate(opcoes):
                classe.criar_linha(tipo='ordenada', ordenacao='esquerda', tamanho=TAMANHO, texto=f'{index + 1}. {opcao}', borda=BORDA)

            classe.criar_linha(tipo='branco', tamanho=TAMANHO)
            classe.criar_linha(tipo='preenchida', tamanho=TAMANHO)
            classe.criar_linha(tipo='vazia', tamanho=TAMANHO)


    # Menu Principal
    @classmethod
    def imprimir_menu_principal(classe, titulo='Sistema de Gerenciamento de Conta', opcoes=['Adicionar', 'Listar', 'Movimentações', 'Editar', 'Sair']):
        classe.imprimir_menu(titulo, titulo, opcoes)


    @classmethod
    def imprimir_menu_mensagem_de_erro(classe, titulo):
        classe.imprimir_menu(titulo, titulo)


    @classmethod
    def imprimir_menu_enter_para_continuar(classe, mensagem_superior, titulo='Pressione "[Enter]" para continuar...'):
        classe.imprimir_menu(mensagem_superior, titulo)


    @classmethod
    def imprimir_menu_sair(classe, titulo='Confirmar "Sair"'):
        classe.imprimir_menu_confirmacao(titulo)


    @classmethod
    def imprimir_menu_confirmacao(classe,tamanho , titulo='Confirmar', opcoes = ['Confirmar', 'Cancelar']):
        classe.imprimir_menu(tamanho, titulo, opcoes)


    @classmethod
    def imprimir_menu_adicionar(classe, titulo='Menu Adicionar', opcoes=['Cliente', 'Conta', 'Voltar']):
        classe.imprimir_menu(titulo, titulo, opcoes)


    def obter_menu_listar():
        return '[ - ] Menu Listar\
            \n[ 1 ] Listar Clientes\
            \n[ 2 ] Listar Contas\
            \n[ 3 ] Voltar'


    def obter_menu_movimentacoes():
        return '[ - ] Menu Movimentações\
            \n[ 1 ] Realizar Depósito\
            \n[ 2 ] Realizar Saque\
            \n[ 3 ] Voltar'
    

    def obter_menu_editar():
        return '[ - ] Menu Editar\
            \n[ 1 ] Editar Cliente\
            \n[ 2 ] Editar Conta\
            \n[ 3 ] Voltar'
