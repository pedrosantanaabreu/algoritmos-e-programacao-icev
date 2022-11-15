from time import sleep
from .utilitarios import Utilitarios
from .cliente import Cliente
from .dados import Dados
from .conta import Conta
from rich import print as rprint
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich.console import Console


class Interfaces:
    @staticmethod
    def imprimir_menu_generico(TITULO_PRINCIPAL='', SUBTITULO='', ):
        TITULO_PRINCIPAL = TITULO_PRINCIPAL
        SUBTITULO = SUBTITULO
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_opcoes.split_row(
            Layout(Panel(Align(Text('Cliente'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Conta'), align='center', vertical='middle'), title='2')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='3')),
        )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)

    # Menu principal
    @staticmethod
    def imprimir_menu_principal():
        TITULO_PRINCIPAL = 'Sistema de Gerenciamento de Contas'
        SUBTITULO = 'Feito por @pedrosantanaabreu'
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes_superior = Layout()
        div_opcoes_inferiror = Layout()
        div_opcoes = Layout()
        
        div_opcoes_superior.split_row(
            Layout(Panel(Align(Text('Adicionar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Editar'), align='center', vertical='middle'), title='2')),
            Layout(Panel(Align(Text('Excluir'), align='center', vertical='middle'), title='3')),
        )

        div_opcoes_inferiror.split_row(
            Layout(Panel(Align(Text('Listar'), align='center', vertical='middle'), subtitle='4')),
            Layout(Panel(Align(Text('Movimentações'), align='center', vertical='middle'), subtitle='5')),
            Layout(Panel(Align(Text('Sair'), align='center', vertical='middle'), subtitle='6')),
        )

        div_opcoes.split_column(
            div_opcoes_superior,
            div_opcoes_inferiror,
        )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @classmethod
    def imprimir_menu_adicionar(cls):
        TITULO_PRINCIPAL = 'Adicionar'
        cls.imprimir_menu_generico(TITULO_PRINCIPAL=TITULO_PRINCIPAL)


    @classmethod
    def imprimir_menu_editar(cls):
        TITULO_PRINCIPAL = 'Editar'
        cls.imprimir_menu_generico(TITULO_PRINCIPAL=TITULO_PRINCIPAL)


    @classmethod
    def imprimir_menu_excluir(cls):
        TITULO_PRINCIPAL = 'Excluir'
        cls.imprimir_menu_generico(TITULO_PRINCIPAL=TITULO_PRINCIPAL)


    @classmethod
    def imprimir_menu_listar(cls):
        TITULO_PRINCIPAL = 'Listar'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes_superior = Layout()
        div_opcoes_inferiror = Layout()
        div_opcoes = Layout()
        
        div_opcoes_superior.split_row(
            Layout(Panel(Align(Text('Cliente'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Conta'), align='center', vertical='middle'), title='2')),
            Layout(Panel(Align(Text('Movimentações'), align='center', vertical='middle'), title='3')),
        )

        div_opcoes_inferiror.split_row(
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), subtitle='4'))
        )

        div_opcoes.split_column(
            div_opcoes_superior,
            div_opcoes_inferiror,
        )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @classmethod
    def imprimir_menu_movimentacoes(cls):
        TITULO_PRINCIPAL = 'Movimentações'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes_superior = Layout()
        div_opcoes_inferiror = Layout()
        div_opcoes = Layout()
        
        div_opcoes_superior.split_row(
            Layout(Panel(Align(Text('Depositar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Sacar'), align='center', vertical='middle'), title='2')),
            Layout(Panel(Align(Text('Transferir'), align='center', vertical='middle'), title='3')),
        )

        div_opcoes_inferiror.split_row(
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), subtitle='4'))
        )

        div_opcoes.split_column(
            div_opcoes_superior,
            div_opcoes_inferiror,
        )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_depositar(agencia : str = '', conta : str = '', valor : str = ''):
        TITULO_PRINCIPAL = 'Depositar'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        if agencia == '':
            SUBTITULO = 'Informe a agência'
        elif conta == '':
            SUBTITULO = 'Informe a conta'
        elif valor == '':
            SUBTITULO = 'Informe o valor'
        else:
            SUBTITULO = 'Confirmação'

        div_opcoes_lateral_esquerda = Layout()
        div_informacoes = Layout()
        div_opcoes = Layout()

        div_informacoes.split_column(
            Layout(Panel(Align(agencia, align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(conta, align='center', vertical='middle'), title='Conta')),
            Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(valor)}', align='center', vertical='middle'), title='Valor')),
        )

        div_opcoes_lateral_esquerda.split_row(
            Layout(Panel(div_informacoes, title='Informações da conta'))
        )

        if valor == '':
            if conta != '':
                _, _, cpf, saldo = Dados.obter_informacoes_bancarias(agencia=agencia, conta=conta)
                nome = Dados.obter_informacoes_pessoais(cpf)

                div_informacoes_pessoais = Layout()
                div_informacoes_pessoais.split_column(
                    Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(cpf), align='center', vertical='middle'), title='CPF')),
                    Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(saldo)}', align='center', vertical='middle'), title='Saldo')),
                    Layout(Panel(Align(nome.title(), align='center', vertical='middle'), title='Conta')),
                )

                div_opcoes.split_row(
                    div_opcoes_lateral_esquerda,
                    Layout(Panel(div_informacoes_pessoais, title='Informações pessoais')),
                    Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
                )
            else:
                div_opcoes.split_row(
                    div_opcoes_lateral_esquerda,
                    Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
                )
        else:
            _, _, cpf, saldo = Dados.obter_informacoes_bancarias(agencia=agencia, conta=conta)
            nome = Dados.obter_informacoes_pessoais(cpf)

            div_informacoes_pessoais = Layout()
            div_informacoes_pessoais.split_column(
                Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(cpf), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(saldo)}', align='center', vertical='middle'), title='Saldo')),
                Layout(Panel(Align(nome.title(), align='center', vertical='middle'), title='Conta')),
            )

            div_opcoes.split_row(
                div_opcoes_lateral_esquerda,
                Layout(Panel(div_informacoes_pessoais, title='Informações pessoais')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
            )

            div_opcoes.split_row(
                div_opcoes_lateral_esquerda,
                Layout(Panel(div_informacoes_pessoais, title='Informações pessoais')),
                Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2')),
            )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_sacar(agencia : str = '', conta : str = '', valor : str = ''):
        TITULO_PRINCIPAL = 'Sacar'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        if agencia == '':
            SUBTITULO = 'Informe a agência'
        elif conta == '':
            SUBTITULO = 'Informe a conta'
        elif valor == '':
            SUBTITULO = 'Informe o valor'
        else:
            SUBTITULO = 'Confirmação'

        div_opcoes_lateral_esquerda = Layout()
        div_informacoes = Layout()
        div_opcoes = Layout()

        div_informacoes.split_column(
            Layout(Panel(Align(agencia, align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(conta, align='center', vertical='middle'), title='Conta')),
            Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(valor)}', align='center', vertical='middle'), title='Valor')),
        )

        div_opcoes_lateral_esquerda.split_row(
            Layout(Panel(div_informacoes, title='Informações da conta'))
        )

        if valor == '':
            if conta != '':
                _, _, cpf, saldo = Dados.obter_informacoes_bancarias(agencia=agencia, conta=conta)
                nome = Dados.obter_informacoes_pessoais(cpf)

                div_informacoes_pessoais = Layout()
                div_informacoes_pessoais.split_column(
                    Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(cpf), align='center', vertical='middle'), title='CPF')),
                    Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(saldo)}', align='center', vertical='middle'), title='Saldo')),
                    Layout(Panel(Align(nome.title(), align='center', vertical='middle'), title='Conta')),
                )

                div_opcoes.split_row(
                    div_opcoes_lateral_esquerda,
                    Layout(Panel(div_informacoes_pessoais, title='Informações pessoais')),
                    Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
                )
            else:
                div_opcoes.split_row(
                    div_opcoes_lateral_esquerda,
                    Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
                )
        else:
            _, _, cpf, saldo = Dados.obter_informacoes_bancarias(agencia=agencia, conta=conta)
            nome = Dados.obter_informacoes_pessoais(cpf)

            div_informacoes_pessoais = Layout()
            div_informacoes_pessoais.split_column(
                Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(cpf), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(saldo)}', align='center', vertical='middle'), title='Saldo')),
                Layout(Panel(Align(nome.title(), align='center', vertical='middle'), title='Conta')),
            )

            div_opcoes.split_row(
                div_opcoes_lateral_esquerda,
                Layout(Panel(div_informacoes_pessoais, title='Informações pessoais')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
            )

            div_opcoes.split_row(
                div_opcoes_lateral_esquerda,
                Layout(Panel(div_informacoes_pessoais, title='Informações pessoais')),
                Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2')),
            )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_transferir(agencia_remetente : str = '', conta_remetente : str = '', agencia_destinatario : str = '', conta_destinatario : str = '', valor : str = ''):
        TITULO_PRINCIPAL = 'Transferir'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1
        
        div_opcoes = Layout()
        div_informacoes_remetente = Layout()
        div_informacoes_destinatario = Layout()

        div_informacoes_remetente.split_column(
            Layout(Panel(Align(agencia_remetente, align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(conta_remetente, align='center', vertical='middle'), title='Conta')),
            Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(valor)}', align='center', vertical='middle'), title='Valor')),
        )

        div_informacoes_destinatario.split_column(
            Layout(Panel(Align(agencia_destinatario, align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(conta_destinatario, align='center', vertical='middle'), title='Conta'))
        )
    
        div_opcoes.split_row(
            Layout(Panel(div_informacoes_remetente, title='Remetente')),
            Layout(Panel(div_informacoes_destinatario, title='Destinatário')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
        )

        if agencia_remetente == '':
            SUBTITULO = 'Informe a agência do remetente'
        elif conta_remetente == '':
            SUBTITULO = 'Informe a conta do remetente'
        elif valor == '':
            SUBTITULO = 'Informe o valor da transferência'
        elif agencia_destinatario == '':
            SUBTITULO = 'Informe a agência do destinatário'
        elif conta_destinatario == '':
            SUBTITULO = 'Informe a conta do destinatário'
        else:
            div_opcoes.split_row(
                Layout(Panel(div_informacoes_remetente, title='Remetente')),
                Layout(Panel(div_informacoes_destinatario, title='Destinatário')),
                Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
            )
            SUBTITULO = 'Confirmação'

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_listar_movimentacoes():
        lista_de_movimentacoes = Dados.obter_lista_de_movimentacoes()

        TITULO_PRINCIPAL = 'Movimentações'
        SUBTITULO = ''
        ALTURA_MAXIMA = 5
        PADDING = 1

        tabela_de_movimentacoes = Table(
            expand=True,
            style='bright_cyan bold',
            show_lines=True
        )

        tabela_de_movimentacoes.add_column('Remetente', style='bright_cyan', header_style='bright_cyan bold')
        tabela_de_movimentacoes.add_column('Destinatário', style='bright_cyan', header_style='bright_cyan bold')
        tabela_de_movimentacoes.add_column('Ação', style='bright_cyan', header_style='bright_cyan bold')
        tabela_de_movimentacoes.add_column('Valor', style='bright_cyan', header_style='bright_cyan bold')
        tabela_de_movimentacoes.add_column('Data', style='bright_cyan', header_style='bright_cyan bold')

        for movimentacao in lista_de_movimentacoes:
            try:
                if movimentacao[0] != 'remetente':
                    try:
                        tabela_de_movimentacoes.add_row(movimentacao[0].title(), movimentacao[1].title(), movimentacao[2].title(), f'R$ {float(movimentacao[3]):.2f}', movimentacao[4])
                    except:
                        pass
                else:
                    pass
            except:
                pass

        menu_principal = Panel(
            Align(Text('Voltar'), align='center', vertical='middle'),
            style='bright_cyan bold',
            title='1',
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(Panel(tabela_de_movimentacoes, style='bright_cyan', title=TITULO_PRINCIPAL))
        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_listar_dados(lista):
        TITULO_PRINCIPAL = f'Listar {lista}'
        SUBTITULO = ''
        ALTURA_MAXIMA = 5
        PADDING = 1

        tabela_de_dados = Table(
            expand=True,
            style='bright_cyan bold',
            show_lines=True
        )

        if lista == 'clientes':
            lista = Dados.obter_lista_de_clientes()

            tabela_de_dados.add_column('Nome', style='bright_cyan', header_style='bright_cyan bold')
            tabela_de_dados.add_column('CPF', style='bright_cyan', header_style='bright_cyan bold')

            for cliente in lista:
                try:
                    if cliente[0] != 'nome':
                        try:
                            tabela_de_dados.add_row(cliente[0].title(), Utilitarios.imprimir_cpf_com_pontuacao(cliente[1]))
                        except:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            lista = Dados.obter_lista_de_contas()

            tabela_de_dados.add_column('Agência', style='bright_cyan', header_style='bright_cyan bold')
            tabela_de_dados.add_column('Conta', style='bright_cyan', header_style='bright_cyan bold')
            tabela_de_dados.add_column('CPF', style='bright_cyan', header_style='bright_cyan bold')
            tabela_de_dados.add_column('Saldo', style='bright_cyan', header_style='bright_cyan bold')

            for conta in lista:
                try:
                    if conta[0] != 'agencia':
                        try:
                            tabela_de_dados.add_row(conta[0], conta[1], Utilitarios.imprimir_cpf_com_pontuacao(conta[2]), f'R$ {float(conta[3]):.2f}')
                        except:
                            pass
                    else:
                        pass
                except:
                    pass

        menu_principal = Panel(
            Align(Text('Voltar'), align='center', vertical='middle'),
            style='bright_cyan bold',
            title='1',
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(Panel(tabela_de_dados, style='bright_cyan', title=TITULO_PRINCIPAL))
        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_sair():
        TITULO_PRINCIPAL = 'Sair'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_opcoes.split_row(
            Layout(Panel(Align(Text('Salvar e sair'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Sair sem salvar'), align='center', vertical='middle'), title='2')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='3')),
        )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_adicionar_cliente(NOME_DO_CLIENTE='', CPF_DO_CLIENTE=''):
        TITULO_PRINCIPAL = 'Adicionando cliente'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1
        
        div_opcoes = Layout()
        div_opcoes_lateral_esquerda = Layout()
        div_confirmacao = Layout()
        
        div_confirmacao.split_row(
            Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
        )

        div_opcoes_lateral_esquerda.split_column(
            Layout(Panel(Align(Text(NOME_DO_CLIENTE), align='center', vertical='middle'), title='Nome')),
            Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(CPF_DO_CLIENTE)), align='center', vertical='middle'), title='CPF'))
        )

        pagina = 0

        if NOME_DO_CLIENTE == '':
            pagina = 1
        elif CPF_DO_CLIENTE == '':
            pagina = 2
        else:
            pagina = 3

        if pagina == 1:
            SUBTITULO = 'Informe o nome'

            div_opcoes.split_row(
                Layout(Panel(div_opcoes_lateral_esquerda, title='Informações do cliente', subtitle=SUBTITULO)),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )
        elif pagina == 2:
            SUBTITULO = 'Informe o CPF'
        
            div_opcoes.split_row(
                Layout(Panel(div_opcoes_lateral_esquerda, title='Informações do cliente', subtitle=SUBTITULO)),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )
        else:
            SUBTITULO = ''

            div_opcoes.split_row(
                Layout(Panel(div_opcoes_lateral_esquerda, title='Informações do cliente', subtitle=SUBTITULO)),
                Panel(div_confirmacao, title='Confirmação necessária'),
            )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle='',
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @classmethod
    def imprimir_menu_editar_cliente(cls):
        cls.imprimir_menu_generico('Editar')


    @staticmethod
    def imprimir_menu_editando_cliente(cliente_antigo : Cliente, cliente_novo : Cliente, opcao):
        TITULO_PRINCIPAL = 'Editar cliente'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_esquerda = Layout()
        div_direita = Layout()
        div_centro = Layout()
        div_confirmacao = Layout()

        div_confirmacao.split_row(
            Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
        )

        if cliente_antigo.cpf == '':
            div_esquerda.split_column(
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente_antigo.cpf)), align='center', vertical='middle'), title='CPF'))
            )

            div_opcoes.split_row(
                Layout(Panel(div_esquerda, title='Informe o CPF')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )
        else:
            if opcao == 1:
                cliente_antigo.nome = Dados.obter_informacoes_pessoais(Utilitarios.formatar_cpf(cliente_antigo.cpf))
                div_esquerda.split_column(
                    Layout(Panel(Align(Text(Utilitarios.formatar_nome(cliente_antigo.nome)), align='center', vertical='middle'), title='Nome')),
                    Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente_antigo.cpf)), align='center', vertical='middle'), title='CPF'))
                )

                div_direita.split_column(
                    Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
                )

                div_opcoes.split_row(
                    Layout(Panel(div_esquerda, title='Informações do cliente')),
                    Layout(Panel(Layout(Panel('', title='Novo nome')), title='Informações novas')),
                    Layout(Panel(div_direita, title='Editar'))
                )
            elif opcao == 2:
                cliente_antigo.nome = Dados.obter_informacoes_pessoais(Utilitarios.formatar_cpf(cliente_antigo.cpf))
                div_esquerda.split_column(
                    Layout(Panel(Align(Text(Utilitarios.formatar_nome(cliente_antigo.nome)), align='center', vertical='middle'), title='Nome')),
                    Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente_antigo.cpf)), align='center', vertical='middle'), title='CPF'))
                )

                div_direita.split_column(
                    Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
                )

                div_opcoes.split_row(
                    Layout(Panel(div_esquerda, title='Informações do cliente')),
                    Layout(Panel(Layout(Panel('', title='Novo CPF')), title='Informações novas')),
                    Layout(Panel(div_direita, title='Editar'))
                )
            else:
                if cliente_novo.cpf != '' or cliente_novo.nome != '':
                    cliente_antigo.nome = Dados.obter_informacoes_pessoais(Utilitarios.formatar_cpf(cliente_antigo.cpf))
                    if cliente_novo.cpf == '':
                        cliente_novo.cpf = cliente_antigo.cpf
                    
                    if cliente_novo.nome == '':
                        cliente_novo.nome = cliente_antigo.nome

                    div_centro.split_column(
                        Layout(Panel(Align(Text(Utilitarios.formatar_nome(cliente_novo.nome)), align='center', vertical='middle'), title='Nome')),
                        Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente_novo.cpf)), align='center', vertical='middle'), title='CPF'))
                    )

                    div_esquerda.split_column(
                        Layout(Panel(Align(Text(Utilitarios.formatar_nome(cliente_antigo.nome)), align='center', vertical='middle'), title='Nome')),
                        Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente_antigo.cpf)), align='center', vertical='middle'), title='CPF'))
                    )

                    div_direita.split_column(
                        Layout(Panel(Align(Text('Nome'), align='center', vertical='middle'), title='1')),
                        Layout(Panel(Align(Text('CPF'), align='center', vertical='middle'), title='2')),
                        Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='3'))
                    )

                    div_opcoes.split_row(
                        Layout(Panel(div_esquerda, title='Informações antigas')),
                        Layout(Panel(div_centro, title='Informações novas')),
                        Layout(Panel(div_confirmacao, title='Confirmação'))
                    )
                else:
                    cliente_antigo.nome = Dados.obter_informacoes_pessoais(Utilitarios.formatar_cpf(cliente_antigo.cpf))
                    div_esquerda.split_column(
                        Layout(Panel(Align(Text(Utilitarios.formatar_nome(cliente_antigo.nome)), align='center', vertical='middle'), title='Nome')),
                        Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente_antigo.cpf)), align='center', vertical='middle'), title='CPF'))
                    )

                    div_direita.split_column(
                        Layout(Panel(Align(Text('Nome'), align='center', vertical='middle'), title='1')),
                        Layout(Panel(Align(Text('CPF'), align='center', vertical='middle'), title='2')),
                        Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='3'))
                    )

                    div_opcoes.split_row(
                        Layout(Panel(div_esquerda, title='Informações do cliente')),
                        Layout(Panel(div_direita, title='Editar'))
                    )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle='',
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    def imprimir_menu_editando_conta(conta_antiga : Conta, conta_nova : Conta, pagina, opcao):
        TITULO_PRINCIPAL = 'Editar conta'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_esquerda = Layout()
        div_confirmacao = Layout()
        div_opcoes_editar = Layout()
        div_esquerda_infos = Layout()

        div_esquerda.split_column(
            Layout(Panel(Align(conta_antiga.agencia, align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(conta_antiga.conta, align='center', vertical='middle'), title='Conta')),

        )

        div_confirmacao.split_row(
            Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
        )

        div_opcoes_editar.split_column(
            Layout(Panel(Align(Text('Agência'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Conta'), align='center', vertical='middle'), title='2')),
            Layout(Panel(Align(Text('CPF'), align='center', vertical='middle'), title='3')),
            Layout(Panel(Align(Text('Saldo'), align='center', vertical='middle'), title='4'))
        )

        if pagina <= 2:
            if conta_antiga.agencia == '':
                SUBTITULO = 'Informe a agência'
            else:
                SUBTITULO = 'Informe a conta'

            div_opcoes.split_row(
                Layout(Panel(div_esquerda, title='Informações sobre a conta', subtitle=SUBTITULO)),
                Layout(Panel(Align('Voltar', align='center', vertical='middle'), title='1'))
            )
        elif pagina == 3:
            _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_antiga.conta)

            div_esquerda.split_column(
                Layout(Panel(Align(_agencia, align='center', vertical='middle'), title='Agência')),
                Layout(Panel(Align(_conta, align='center', vertical='middle'), title='Conta')),
                Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(_cpf), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(_saldo)}', align='center', vertical='middle'), title='Saldo')),
            )
            div_opcoes.split_row(
                Layout(Panel(div_esquerda, title='Informações sobre a conta', subtitle=SUBTITULO)),
                Layout(Panel(div_opcoes_editar, title='Editar')),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='5')),
            )
        elif pagina == 4:
            if opcao == 1:
                titulo = 'Informe a nova agência'
            elif opcao == 2:
                titulo = 'Informe a nova conta'
            elif opcao == 3:
                titulo = 'Informe o novo CPF'
            else:
                titulo = 'Informe o novo saldo'
            
            _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_antiga.conta)

            div_esquerda.split_column(
                Layout(Panel(Align(_agencia, align='center', vertical='middle'), title='Agência')),
                Layout(Panel(Align(_conta, align='center', vertical='middle'), title='Conta')),
                Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(_cpf), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(_saldo)}', align='center', vertical='middle'), title='Saldo')),
            )

            div_opcoes.split_row(
                Layout(Panel(div_esquerda, title='Informações sobre a conta')),
                Layout(Panel('', title=titulo)),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
            )
        elif pagina == 5:
            _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_antiga.conta)


            div_esquerda.split_column(
                Layout(Panel(Align(_agencia, align='center', vertical='middle'), title='Agência')),
                Layout(Panel(Align(_conta, align='center', vertical='middle'), title='Conta')),
                Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(_cpf), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(_saldo)}', align='center', vertical='middle'), title='Saldo')),
            )

            div_esquerda_infos.split_column(
                Layout(Panel(Align(conta_nova.agencia, align='center', vertical='middle'), title='Agência')),
                Layout(Panel(Align(conta_nova.conta, align='center', vertical='middle'), title='Conta')),
                Layout(Panel(Align(Utilitarios.imprimir_cpf_com_pontuacao(conta_nova.cpf), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(f'R$ {Utilitarios.formatar_dinheiro(conta_nova.saldo)}', align='center', vertical='middle'), title='Saldo')),
            )

            div_opcoes.split_row(
                Layout(Panel(div_esquerda, title='Conta antiga')),
                Layout(Panel(div_esquerda_infos, title='Conta nova')),
                Layout(Panel(div_confirmacao, title='1'))
            )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle='',
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_adicionar_conta(agencia='', conta='', cpf='', saldo=''):
        TITULO_PRINCIPAL = 'Adicionando conta'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_informacoes_lateral_esquerda = Layout()
        div_confirmar = Layout()
        div_informacoes_pessoas_direita = Layout()

        div_confirmar.split_row(
        Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
        Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
        )

        div_informacoes_lateral_esquerda.split_column(
            Layout(Panel(Align(Text(agencia), align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(Text(conta), align='center', vertical='middle'), title='Conta')),
            Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cpf)), align='center', vertical='middle'), title='CPF')),
            Layout(Panel(Align(Text(f'R$ {saldo}'), align='center', vertical='middle'), title='Saldo inicial'))
        )



        pagina = 0
        if agencia == '':
            pagina = 1

            SUBTITULO = 'Informe a agência'
        elif conta == '':
            pagina = 2

            SUBTITULO = 'Informe o número da conta'
        elif cpf == '':
            pagina = 3

            SUBTITULO = 'Informe o CPF'
        elif saldo == '':
            pagina = 4

            SUBTITULO = 'Informe o saldo inicial'
        else:
            pagina = 5

            SUBTITULO = 'Confirmação necessária'
    


        if pagina < 4:
            div_opcoes.split_row(
                Panel(div_informacoes_lateral_esquerda, title='Informaçõs sobre a conta', subtitle=SUBTITULO),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )
        elif pagina < 5:
            cliente = Cliente()
            cliente.cpf = Utilitarios.formatar_cpf(cpf)
            cliente.nome = Dados.obter_informacoes_pessoais(cliente.cpf)

            div_informacoes_pessoas_direita.split_column(
                Layout(Panel(Align(Text(cliente.nome), align='center', vertical='middle'), title='Nome')),
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente.cpf)), align='center', vertical='middle'), title='CPF')),
            )

            div_opcoes.split_row(
                Panel(div_informacoes_lateral_esquerda, title='Informaçõs sobre a conta', subtitle=SUBTITULO),
                Panel(div_informacoes_pessoas_direita, title='Informações pessoais'),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )
        elif pagina == 5:
            cliente = Cliente()
            cliente.cpf = Utilitarios.formatar_cpf(cpf)
            cliente.nome = Dados.obter_informacoes_pessoais(cliente.cpf)
            
            div_informacoes_pessoas_direita.split_column(
                Layout(Panel(Align(Text(cliente.nome), align='center', vertical='middle'), title='Nome')),
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente.cpf)), align='center', vertical='middle'), title='CPF')),
            )

            div_opcoes.split_row(
                Panel(div_informacoes_lateral_esquerda, title='Informaçõs sobre a conta', subtitle=SUBTITULO),
                Panel(div_informacoes_pessoas_direita, title='Informações pessoais'),
                Panel(div_confirmar, title='Confirmação necessária'),
            )
        else:
            pass


        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle='',
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_excluir_cliente(cpf=''):
        TITULO_PRINCIPAL = 'Excluindo cliente'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_informacoes_esquerda = Layout()
        div_informacoes_internas = Layout()
        div_dados_bancarios = Layout()
        div_dados_pessoais = Layout()
        div_confirmacao = Layout()
        
        div_confirmacao.split_row(
            Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
        )

        if cpf == '':
            div_informacoes_esquerda.split_column(
                Layout(Panel(Layout(Panel('', title='CPF')), title='Informe o CPF do cliente que deseja excluir')),
            )

            div_opcoes.split_row(
                div_informacoes_esquerda,
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1')),
            )
        else:
            nome = Dados.obter_informacoes_pessoais(Utilitarios.formatar_cpf(cpf))
            try:
                agencia, conta, cpf, saldo = Dados.obter_informacoes_bancarias(cpf=cpf)
            except:
                agencia, conta, cpf, saldo = ['0000', '000000000', cpf, '0']

            div_dados_bancarios.split_column(
                
                Layout(Panel(Align(Text(agencia), align='center', vertical='middle'), title='Agência')),
                Layout(Panel(Align(Text(conta), align='center', vertical='middle'), title='Conta')),
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cpf)), align='center', vertical='middle'), title='CPF')),
                Layout(Panel(Align(Text(f'R$ {float(saldo):.2f}'), align='center', vertical='middle'), title='Saldo')),
            )

            div_dados_pessoais.split_column(
                Layout(Panel(Align(Text(nome), align='center', vertical='middle'), title='Nome')),
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cpf)), align='center', vertical='middle'), title='CPF')),
            )
    
            div_informacoes_internas.split_row(
                Layout(Panel(div_dados_bancarios, title='Dados bancários')),
                Layout(Panel(div_dados_pessoais, title='Dados pessoais'))
            )
    
            div_informacoes_esquerda.split_column(
                Layout(Panel(div_informacoes_internas, title='Dados do cliente')),
            )


            div_opcoes.split_row(
                div_informacoes_esquerda,
                Layout(Panel(div_confirmacao, title='Confirmar em excluir os dados do cliente'))
            )


        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle='',
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_excluir_conta(conta : Conta):
        TITULO_PRINCIPAL = 'Excluindo conta'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        div_informacoes_lateral_esquerda = Layout()
        div_confirmar = Layout()
        div_informacoes_pessoas_direita = Layout()

        div_confirmar.split_row(
        Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
        Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='2'))
        )

        div_informacoes_lateral_esquerda.split_column(
            Layout(Panel(Align(Text(conta.agencia), align='center', vertical='middle'), title='Agência')),
            Layout(Panel(Align(Text(conta.conta), align='center', vertical='middle'), title='Conta'))
        )



        pagina = 0
        if conta.agencia == '':
            pagina = 1

            SUBTITULO = 'Informe a agência'
        elif conta.conta == '':
            pagina = 2

            SUBTITULO = 'Informe o número da conta'
        else:
            pagina = 3

            SUBTITULO = 'Confirmação necessária'
    


        if pagina < 3:
            div_opcoes.split_row(
                Panel(div_informacoes_lateral_esquerda, title='Informaçõs sobre a conta', subtitle=SUBTITULO),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )
        else:
            _, _, _cpf, _ = Dados.obter_informacoes_bancarias(agencia=conta.agencia, conta=conta.conta)

            cliente = Cliente()
            cliente.cpf = Utilitarios.formatar_cpf(_cpf)
            cliente.nome = Dados.obter_informacoes_pessoais(cliente.cpf)

            div_informacoes_pessoas_direita.split_column(
                Layout(Panel(Align(Text(cliente.nome), align='center', vertical='middle'), title='Nome')),
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente.cpf)), align='center', vertical='middle'), title='CPF')),
            )

            div_opcoes.split_row(
                Panel(div_informacoes_lateral_esquerda, title='Informaçõs sobre a conta', subtitle=SUBTITULO),
                Panel(div_informacoes_pessoas_direita, title='Informações pessoais'),
                Layout(Panel(Align(Text('Voltar'), align='center', vertical='middle'), title='1'))
            )

            
            div_informacoes_pessoas_direita.split_column(
                Layout(Panel(Align(Text(cliente.nome), align='center', vertical='middle'), title='Nome')),
                Layout(Panel(Align(Text(Utilitarios.imprimir_cpf_com_pontuacao(cliente.cpf)), align='center', vertical='middle'), title='CPF')),
            )

            div_opcoes.split_row(
                Panel(div_informacoes_lateral_esquerda, title='Informaçõs sobre a conta', subtitle=SUBTITULO),
                Panel(div_informacoes_pessoas_direita, title='Informações pessoais'),
                Panel(div_confirmar, title='Confirmação necessária'),
            )


        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle='',
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    # Outros
    @staticmethod
    def imprimir_input():
        rprint('[bright_cyan bold]| -> [/]', end='')
    

    @staticmethod
    def imprimir_menu_confirmacao():
        TITULO_PRINCIPAL = 'Confirmação'
        SUBTITULO = ''
        ALTURA_MAXIMA = 20
        PADDING = 1

        div_opcoes = Layout()
        
        div_opcoes.split_row(
            Layout(Panel(Align(Text('Confirmar'), align='center', vertical='middle'), title='1')),
            Layout(Panel(Align(Text('Cancelar'), align='center', vertical='middle'), title='2')),
        )

        menu_principal = Panel(
            div_opcoes,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)


    @staticmethod
    def imprimir_menu_mensagem_de_erro(mensagem):
        TITULO_PRINCIPAL = 'Aviso'
        SUBTITULO = 'Pressione [ Enter ] para continuar'
        ALTURA_MAXIMA = 20
        PADDING = 1

        TEXTO = Align(mensagem, align='center', vertical='middle')
        menu_principal = Panel(
            TEXTO,
            style='red bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu_principal)
        rprint('[red bold]| -> [/]', end=''); input()


    @staticmethod
    def imprimir_menu_mensagem_de_conclusao(MENSAGEM):
        TITULO_PRINCIPAL = 'Concluído'
        SUBTITULO = 'Pressione [ Enter ] para continuar'
        ALTURA_MAXIMA = 20
        PADDING = 1

        TEXTO = Align(Text(MENSAGEM), align='center', vertical='middle')
        menu = Panel(
            TEXTO,
            style='bright_cyan bold',
            title=TITULO_PRINCIPAL,
            subtitle=SUBTITULO,
            height=ALTURA_MAXIMA,
            padding=PADDING
        )

        rprint(menu)
        rprint('[bright_cyan bold]| -> [/]', end=''); input()
