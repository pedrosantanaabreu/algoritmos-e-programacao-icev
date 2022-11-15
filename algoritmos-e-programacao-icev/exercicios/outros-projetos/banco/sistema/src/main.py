from .interfaces import Interfaces
from .utilitarios import Utilitarios
from .validadores import Validadores
from .conta import Conta
from .dados import Dados
from .cliente import Cliente
from .movimentacao import Movimentacao
from datetime import datetime
from rich import print as rprint
import zipfile


class Main:
    @classmethod
    def iniciar_aplicacao(cls):
        cls.__menu_principal()
    

    # Menu principal
    @classmethod
    def __menu_principal(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_principal()
            Interfaces.imprimir_input()
            opcao_usuario_menu_principal = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_principal, 6):
                cls.__opcoes_menu_principal(int(opcao_usuario_menu_principal))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_principal}" é inválido.')

  
    @classmethod
    def __opcoes_menu_principal(cls, opcao_usuario_menu_principal : int):
        if opcao_usuario_menu_principal == 1:
            cls.__menu_adicionar()
        elif opcao_usuario_menu_principal == 2:
            cls.__menu_editar()
        elif opcao_usuario_menu_principal == 3:
            cls.__menu_excluir()
        elif opcao_usuario_menu_principal == 4:
            cls.__menu_listar()
        elif opcao_usuario_menu_principal == 5:
            cls.__menu_movimentacoes()
        elif opcao_usuario_menu_principal == 6:
            cls.__menu_sair()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_principal}" é inválido.')

    # Editar
    @classmethod
    def __menu_editar(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_editar_cliente()
            Interfaces.imprimir_input()
            opcao_usuario_menu_editar = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_editar, 3):
                if int(opcao_usuario_menu_editar) == 3:
                    break
                else:
                    cls.__opcoes_menu_editar(int(opcao_usuario_menu_editar))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_editar}" é inválido.') 


    @classmethod
    def __opcoes_menu_editar(cls, opcao_usuario_menu_editar):
        if opcao_usuario_menu_editar == 1:
            cls.__editar_cliente()
        elif opcao_usuario_menu_editar == 2:
            cls.__editar_conta()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_editar}" é inválido.') 


    @classmethod
    def __editar_cliente(cls):
        cliente_antigo = Cliente()
        cliente_novo = Cliente()

        opcao = 0
        pagina = 1
        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_editando_cliente(cliente_antigo, cliente_novo, opcao)

            if pagina == 1:
                cliente_antigo.cpf = cls.__obter_cpf_cliente()

                if cliente_antigo.cpf == 1:
                    cliente_antigo.cpf = ''
                    pagina -= 1
                elif cliente_antigo.cpf == 0:
                    cliente_antigo.cpf = ''
                else:
                    if Dados.verificar_cliente_existe(cliente_antigo):
                        pagina += 1
                        cliente_antigo.cpf = Utilitarios.formatar_cpf(cliente_antigo.cpf)
                        cliente_antigo.nome = Dados.obter_informacoes_pessoais(cliente_antigo.cpf)
                    else:
                        cliente_antigo.cpf = ''
                        cliente_antigo.nome = ''
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'Cliente não cadastrado.') 
            elif pagina == 2:
                Interfaces.imprimir_input()
                resposta = input()

                if Validadores.validar_opcao_menu(resposta, 3):
                    if int(resposta) == 3:
                        pagina -= 1
                        cliente_antigo.cpf = ''
                    else:
                        if int(resposta) == 1:
                            opcao = 1
                            pagina += 1
                        else:
                            opcao = 2
                            pagina += 1
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{resposta}" é inválido.')
            elif pagina == 3:
                if opcao == 1:
                    cliente_novo.nome = cls.__obter_nome_cliente()

                    if cliente_novo.nome == 1:
                        cliente_novo.nome = ''

                        pagina -= 1
                        opcao = 0
                    elif cliente_novo.nome == 0:
                        cliente_novo.nome = ''
                    else:
                        if Utilitarios.formatar_nome(cliente_antigo.nome) == Utilitarios.formatar_nome(cliente_novo.nome):
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'O nome novo não pode ser igual ao anterior.')
                            cliente_novo.nome = ''
                        else:
                            pagina += 1
                            opcao = 0
                else:
                    cliente_novo.cpf = cls.__obter_cpf_cliente()

                    if cliente_novo.cpf == 1:
                        cliente_novo.cpf = ''

                        pagina -= 1
                        opcao = 0
                    elif cliente_novo.cpf == 0:
                        cliente_novo.cpf = ''
                    else:
                        if Utilitarios.formatar_cpf(cliente_antigo.cpf) == Utilitarios.formatar_cpf(cliente_novo.cpf):
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'O CPF novo não pode ser igual ao anterior.')
                            cliente_novo.cpf = ''
                        else:
                            cliente_novo.cpf = Utilitarios.formatar_cpf(cliente_novo.cpf)
                            if Dados.verificar_cliente_existe(cliente_novo):
                                Utilitarios.limpar_terminal()
                                Interfaces.imprimir_menu_mensagem_de_erro(f'Cliente já cadastrado.') 
                                cliente_novo.cpf = ''
                            else:
                                pagina += 1
                                opcao = 0
            else:
                Interfaces.imprimir_input()
                confirmacao = input()

                if Validadores.validar_opcao_menu(confirmacao, 2):
                    if int(confirmacao) == 1:
                        cls.__editar_cliente_banco_dados(cliente_antigo, cliente_novo)
                        if cliente_novo.cpf != cliente_antigo.cpf:
                            while Dados.verificar_cpf_cadastrado_em_conta(cliente_antigo.cpf):
                                _agencia_antiga, _conta_antiga, _cpf_antigo, _saldo_antigo = Dados.obter_informacoes_bancarias(cpf=cliente_antigo.cpf)

                                conta_antiga = Conta(_agencia_antiga, _conta_antiga, _cpf_antigo, _saldo_antigo)
                                conta_nova = Conta(_agencia_antiga, _conta_antiga, cliente_novo.cpf, _saldo_antigo)

                                Dados.editar_conta(conta_antiga, conta_nova)
                        else:
                            pass
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_conclusao('Alteração realizada com sucesso')
                        break
                    else:
                        if cliente_novo.nome != cliente_antigo.nome:
                            cliente_novo.nome = ''
                            cliente_novo.cpf = ''
                            opcao = 1
                            pagina -= 1
                        else:
                            cliente_novo.cpf = ''
                            cliente_novo.nome = ''
                            opcao = 2
                            pagina -= 1


    @staticmethod
    def __editar_cliente_banco_dados(cliente_antigo : Cliente, cliente_novo : Cliente):
        Dados.editar_cliente(cliente_antigo=cliente_antigo, cliente_novo=cliente_novo)


    @staticmethod
    def __editar_conta_banco_dados(conta_antiga : Conta, conta_nova : Conta):
        Dados.editar_conta(conta_antiga, conta_nova)


    @classmethod
    def __editar_conta(cls):
        conta_antiga = Conta()
        conta_nova = Conta()
        
        opcao = 0
        pagina = 1
        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_editando_conta(conta_antiga, conta_nova, pagina, opcao)
            
            if pagina == 1:
                conta_antiga.agencia = cls.__obter_agencia()

                if conta_antiga.agencia == 1:
                    pagina -= 1
                    conta_antiga.agencia = ''
                elif conta_antiga.agencia == 0:
                    conta_antiga.agencia = ''
                else:
                    pagina += 1

            elif pagina == 2:
                conta_antiga.conta = cls.__obter_conta_cliente()

                if conta_antiga.conta == 1:
                    pagina = 1
                    conta_antiga.conta = ''
                    conta_antiga.agencia = ''
                elif conta_antiga.conta == 0:
                    conta_antiga.conta = ''
                else:
                    pagina += 1
            elif pagina == 3:
                __agencia, __conta, __cpf, __saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_antiga.conta)
                conta_antiga.cpf = __cpf
                conta_antiga.saldo = __saldo

                Interfaces.imprimir_input()
                item_editar = input()

                if Validadores.validar_opcao_menu(item_editar, 5):
                    if int(item_editar) == 5:
                        conta_antiga.conta = ''
                        pagina -= 1
                    else:
                        opcao = int(item_editar)
                        pagina += 1
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{item_editar}" é inválido.')
            elif pagina == 4:
                if int(item_editar) == 1:
                    conta_nova.agencia = cls.__obter_agencia()

                    if conta_nova.agencia == 1:
                        pagina -= 1
                        conta_nova.agencia = ''
                    elif conta_nova.agencia == 0:
                        conta_nova.agencia = ''
                    else:
                        if conta_nova.agencia == conta_antiga.agencia:
                            conta_nova.agencia = ''
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'A nova conta não pode ser igual a anterior.')
                        else:
                            try:
                                _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_nova.agencia, conta=conta_antiga.conta)
                                conta_nova = Conta()
                                Utilitarios.limpar_terminal()
                                Interfaces.imprimir_menu_mensagem_de_erro(f'Conta já cadastrada.')
                            except:
                                conta_nova.conta = conta_antiga.conta
                                conta_nova.saldo = conta_antiga.saldo
                                conta_nova.cpf = conta_antiga.cpf
                                pagina += 1

                elif int(item_editar) == 2:
                    conta_nova.conta = cls.__obter_conta_cliente()

                    if conta_nova.conta == 1:
                        pagina -= 1
                        conta_nova.conta = ''
                    elif conta_nova.conta == 0:
                        conta_nova.conta = ''
                    else:
                        if conta_antiga.conta == conta_nova.conta:
                            conta_nova.conta = ''
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'A conta nova não pode ser igual a anterior.')
                        else:
                            try:
                                _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_nova.conta)
                                conta_nova = Conta()
                                Utilitarios.limpar_terminal()
                                Interfaces.imprimir_menu_mensagem_de_erro(f'Conta já cadastrada.')
                            except:
                                conta_nova.cpf = conta_antiga.cpf
                                conta_nova.saldo = conta_antiga.saldo
                                conta_nova.agencia = conta_antiga.agencia
                                pagina += 1
                elif int(item_editar) == 3:
                    conta_nova.cpf = cls.__obter_cpf_cliente()

                    if conta_nova.cpf == 1:
                        pagina -= 1
                        conta_nova.cpf = ''
                    elif conta_nova.cpf == 0:
                        conta_nova.cpf = ''
                    else:
                        conta_nova.cpf = Utilitarios.formatar_cpf(conta_nova.cpf)

                        _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_antiga.conta)
                        if _cpf == conta_nova.cpf:
                            conta_nova.cpf = ''
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'O CPF novo não pode ser igual a anterior.')
                        else:
                            cliente = Cliente('', conta_nova.cpf)
                            if Dados.verificar_cliente_existe(cliente):
                                conta_nova.saldo = conta_antiga.saldo
                                conta_nova.conta = conta_antiga.conta
                                conta_nova.agencia = conta_antiga.agencia
                                pagina += 1
                            else:
                                conta_nova = Conta()
                                Utilitarios.limpar_terminal()
                                Interfaces.imprimir_menu_mensagem_de_erro(f'Cliente não cadastrado.')
                else:
                    conta_nova.saldo = cls.__obter_saldo_cliente()

                    if conta_nova.saldo == 1:
                        pagina -= 1
                        conta_nova.saldo = ''
                    elif conta_nova.saldo == 0:
                        conta_nova.saldo = ''
                    else:
                        _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(agencia=conta_antiga.agencia, conta=conta_antiga.conta)
                        if float(_saldo) == float(conta_nova.saldo):
                            conta_nova.cpf = ''
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'O saldo novo não pode ser igual a anterior.')
                        else:
                            conta_nova.cpf = conta_antiga.cpf
                            conta_nova.conta = conta_antiga.conta
                            conta_nova.agencia = conta_antiga.agencia
                            pagina += 1 
            elif pagina == 5:
                Interfaces.imprimir_input()
                confirmacao = input()

                if Validadores.validar_opcao_menu(confirmacao, 2):
                    if int(confirmacao) == 1:
                        cls.__editar_conta_banco_dados(conta_antiga, conta_nova)
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_conclusao('Alteração realizada com sucesso')
                        pagina = 1

                        conta_antiga = Conta()
                        conta_nova = Conta()
                    else:
                        conta_nova = Conta()
                        pagina -= 1


    # Excluir
    @classmethod
    def __menu_excluir(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_excluir()
            Interfaces.imprimir_input()
            opcao_usuario_menu_excluir = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_excluir, 3):
                if int(opcao_usuario_menu_excluir) == 3:
                    break
                else:
                    cls.__opcoes_menu_excluir(int(opcao_usuario_menu_excluir))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_excluir}" é inválido.') 


    @classmethod
    def __opcoes_menu_excluir(cls, opcao_usuario_menu_excluir):
        if opcao_usuario_menu_excluir == 1:
            cls.__excluir_cliente()
        elif opcao_usuario_menu_excluir == 2:
            cls.__excluir_conta()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_excluir}" é inválido.') 
    
    
    @classmethod
    def __excluir_cliente(cls):
        cliente = Cliente()
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_excluir_cliente(cliente.cpf)

            if pagina == 1:
                cpf_cliente = cls.__obter_cpf_cliente()

                if cpf_cliente == 1:
                    pagina -= 1
                    cliente.nome = ''

                elif cpf_cliente == 0:
                    pass
                else:
                    cpf_cliente = Utilitarios.formatar_cpf(cpf_cliente)
                    cliente.cpf = cpf_cliente

                    if Dados.verificar_cliente_existe(cliente):
                        cliente.nome = Dados.obter_informacoes_pessoais(cpf_cliente)
                        pagina += 1
                    else:
                        cliente.cpf = ''
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro('Cliente não cadastrado')
            elif pagina == 2:
                rprint('[bright_cyan bold]| -> [/]', end=''); opcao_menu_excluir = input().strip()

                if opcao_menu_excluir == '1':
                    agencia, conta, cpf, saldo = Dados.obter_informacoes_bancarias(cpf=cliente.cpf)
                    conta = Conta(agencia, conta, cpf, saldo)

                    Dados.del_cliente(cliente)
                    Dados.del_conta(conta)

                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_conclusao('Cliente excluido com sucesso')
                    break
                else:
                    cliente.cpf = ''
                    pagina -= 1
            else:
                break


    @classmethod
    def __excluir_conta(cls):
        conta = Conta()
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_excluir_conta(conta)

            if pagina == 1:
                conta.agencia = cls.__obter_agencia()

                if conta.agencia == 1:
                    pagina -= 1
                elif conta.agencia == 0:
                    conta.agencia = ''
                    pass
                else:
                    pagina += 1
            elif pagina == 2:
                conta.conta = cls.__obter_conta_cliente()

                if conta.conta == 1:
                    pagina -= 1
                    conta.conta = ''
                    conta.agencia = ''
                elif conta.conta == 0:
                    conta.conta = ''
                    pass
                else:
                    if Dados.verificar_conta_existe(conta):
                        pagina += 1
                    else:
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro('Conta não cadastrado')
            elif pagina == 3:
                rprint('[bright_cyan bold]| -> [/]', end='')
                confirmacao_adicionar_conta = input().strip()

                if Validadores.validar_opcao_menu(confirmacao_adicionar_conta, 2):
                    if int(confirmacao_adicionar_conta) == 1:
                        _, _, cpf, saldo = Dados.obter_informacoes_bancarias(agencia=conta.agencia, conta=conta.conta)
                        conta.cpf = cpf
                        conta.saldo = saldo

                        Dados.del_conta(conta)
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_conclusao('Conta excluida com sucesso.')
                        break
                    else:
                        conta.conta = ''
                        pagina -= 1
            else:
                break


    # Menu listar
    @classmethod
    def __menu_listar(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_listar()
            Interfaces.imprimir_input()
            opcao_usuario_menu_listar = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_listar, 4):
                if int(opcao_usuario_menu_listar) == 4:
                    break
                else:
                    cls.__opcoes_menu_listar(int(opcao_usuario_menu_listar))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_listar}" é inválido.') 


    @classmethod
    def __opcoes_menu_listar(cls, opcao_usuario_menu_listar : int):
        if opcao_usuario_menu_listar == 1:
            cls.__menu_listar_clientes()
        elif opcao_usuario_menu_listar == 2:
            cls.__menu_listar_contas()
        elif opcao_usuario_menu_listar == 3:
            cls.__menu_listar_movimentacoes()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_listar}" é inválido.')


    @staticmethod
    def __menu_listar_clientes():
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_listar_dados('clientes')
            Interfaces.imprimir_input()
            opcao_usuario_menu_listar_clientes = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_listar_clientes, 1):
                if int(opcao_usuario_menu_listar_clientes) == 1:
                    break
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_listar_clientes}" é inválido.')
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_listar_clientes}" é inválido.')


    @staticmethod
    def __menu_listar_contas():
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_listar_dados('contas')
            Interfaces.imprimir_input()
            opcao_usuario_menu_listar_contas = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_listar_contas, 1):
                if int(opcao_usuario_menu_listar_contas) == 1:
                    break
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_listar_contas}" é inválido.')
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_listar_contas}" é inválido.')


    @staticmethod
    def __menu_listar_movimentacoes():
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_listar_movimentacoes()
            Interfaces.imprimir_input()
            opcao_usuario_menu_movimentacoes = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_movimentacoes, 1):
                if int(opcao_usuario_menu_movimentacoes) == 1:
                    break
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_movimentacoes}" é inválido.')
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_movimentacoes}" é inválido.')

    # Adicionar
    @classmethod
    def __menu_adicionar(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_adicionar()
            Interfaces.imprimir_input()
            opcao_usuario_menu_adicionar = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_adicionar, 3):
                if int(opcao_usuario_menu_adicionar) == 3:
                    break
                else:
                    cls.__opcoes_menu_adicionar(int(opcao_usuario_menu_adicionar))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_adicionar}" é inválido.')
    

    @classmethod
    def __opcoes_menu_adicionar(cls, opcao_usuario_menu_movimentacoes):
        if opcao_usuario_menu_movimentacoes == 1:
            cls.__adicionar_cliente()
        elif opcao_usuario_menu_movimentacoes == 2:
            cls.__adicionar_conta()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_movimentacoes}" é inválido.')


    @classmethod
    def __adicionar_cliente(cls):
        cliente = Cliente()
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_adicionar_cliente(cliente.nome, cliente.cpf)
            if pagina == 1:
                nome_cliente = cls.__obter_nome_cliente()

                if nome_cliente == 1:
                    pagina -= 1
                elif nome_cliente == 0:
                    pass
                else:
                    cliente.nome = Utilitarios.formatar_nome(nome_cliente)
                    pagina += 1
            elif pagina == 2:
                cpf_cliente = cls.__obter_cpf_cliente()

                if cpf_cliente == 1:
                    pagina -= 1
                    cliente.nome = ''

                elif cpf_cliente == 0:
                    pass
                else:
                    cliente.cpf = Utilitarios.formatar_cpf(cpf_cliente)
                    if Dados.verificar_cliente_existe(cliente):
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro('Cliente já cadastrado')
                        cliente.cpf = ''
                    else:
                        pagina += 1
            elif pagina == 3:
                rprint('[bright_cyan bold]| -> [/]', end='')
                confirmacao_adicionar_cliente = input().strip()

                if Validadores.validar_opcao_menu(confirmacao_adicionar_cliente, 2):
                    if int(confirmacao_adicionar_cliente) == 1:
                        cls.__adicionar_cliente_no_banco(cliente)
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_conclusao('Cliente adicionado com sucesso.')
                        break
                    else:
                        cliente.cpf = ''
                        pagina -= 1
            else:
                break


    @classmethod
    def __adicionar_conta(cls):
        conta = Conta()
        cliente = Cliente()
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_adicionar_conta(conta.agencia, conta.conta, conta.cpf, conta.saldo)
            if pagina == 1:
                agencia_cliente = cls.__obter_agencia_cliente()

                if agencia_cliente == 1:
                    pagina -= 1
                elif agencia_cliente == 0:
                    pass
                else:
                    conta.agencia = agencia_cliente
                    pagina += 1
            
            elif pagina == 2:
                conta_cliente = cls.__obter_conta_cliente()
        
                if conta_cliente == 1:
                    pagina -= 1
                    conta.agencia = ''
                elif conta_cliente == 0:
                    pass
                else:
                    if Dados.verificar_conta_existe(conta):
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro('Conta já cadastrado')
                    else:
                        conta.conta = conta_cliente
                        pagina += 1

            elif pagina == 3:
                cpf_cliente = cls.__obter_cpf_cliente()

                if cpf_cliente == 1:
                    pagina -= 1
                    conta.conta = ''

                elif cpf_cliente == 0:
                    pass
                else:
                    cliente.cpf = cpf_cliente

                    if Dados.verificar_cliente_existe(cliente):
                        conta.cpf = Utilitarios.formatar_cpf(cpf_cliente)
                        pagina += 1
                    else:
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro('Cliente não cadastrado')
                        cliente.cpf = ''
            elif pagina == 4:
                saldo = cls.__obter_saldo_cliente()

                if saldo == 1:
                    pagina -= 1
                    conta.cpf = ''

                elif saldo == 0:
                    pass
                else:
                    conta.saldo = saldo
                    pagina += 1
            elif pagina == 5:
                rprint('[bright_cyan bold]| -> [/]', end='')
                confirmacao_adicionar_conta = input().strip()

                if Validadores.validar_opcao_menu(confirmacao_adicionar_conta, 2):
                    if int(confirmacao_adicionar_conta) == 1:
                        cls.__adicionar_conta_banco(conta)
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_conclusao('Conta criada com sucesso.')
                        break
                    else:
                        conta.saldo = ''
                        pagina -= 1
            else:
                break


    @staticmethod
    def __adicionar_conta_banco(conta : Conta):
        Dados.add_conta(conta)  


    @staticmethod
    def __obter_saldo_cliente():
        rprint('[bright_cyan bold]| -> [/]', end=''); saldo = input().strip()

        if saldo == '1':
            return 1
        else:
            if Validadores.validar_valor_financeiro(saldo):
                return saldo
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{saldo}" é inválido.')
                return 0


    @staticmethod
    def __obter_agencia_cliente():
        rprint('[bright_cyan bold]| -> [/]', end=''); numero_agencia = input().strip()

        if numero_agencia == '1':
            return 1
        else:
            if Validadores.validar_numero_da_agencia(numero_agencia):
                return numero_agencia
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{numero_agencia}" é inválido.')
                return 0


    @staticmethod
    def __obter_nome_cliente(opcao_sair='1'):
        rprint('[bright_cyan bold]| -> [/]', end=''); nome_cliente = input().strip()

        if nome_cliente == opcao_sair:
            return 1
        else:
            if Validadores.validar_nome(nome_cliente):
                return nome_cliente
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{nome_cliente}" é inválido.')
                return 0


    @staticmethod
    def __obter_cpf_cliente(opcao_sair='1'):
        rprint('[bright_cyan bold]| -> [/]', end=''); cpf = input().strip()

        if cpf == opcao_sair:
            return 1
        else:
            if Validadores.validar_cpf(cpf):
                return cpf
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{cpf}" é inválido.')
                return 0
                

    @staticmethod
    def __adicionar_cliente_no_banco(cliente : Cliente):
        Dados.add_cliente(cliente)


    # Menu movimentações
    @classmethod
    def __menu_movimentacoes(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_movimentacoes()
            Interfaces.imprimir_input()
            opcao_usuario_menu_movimentacoes = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_movimentacoes, 4):
                if int(opcao_usuario_menu_movimentacoes) == 4:
                    break
                else:
                    cls.__opcoes_menu_movimentacoes(int(opcao_usuario_menu_movimentacoes))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_movimentacoes}" é inválido.')


    @classmethod
    def __opcoes_menu_movimentacoes(cls, opcao_usuario_menu_movimentacoes):
        if opcao_usuario_menu_movimentacoes == 1:
            cls.__depositar()
        elif opcao_usuario_menu_movimentacoes == 2:
            cls.__sacar()
        elif opcao_usuario_menu_movimentacoes == 3:
            cls.__transferir()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_movimentacoes}" é inválido.') 


    # Sacar
    @classmethod
    def __sacar(cls):
        conta_cliente = Conta()
        valor = ''
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_sacar(conta_cliente.agencia, conta_cliente.conta, valor)

            if pagina == 1:
                conta_cliente.agencia = cls.__obter_agencia()

                if conta_cliente.agencia == 1:
                    conta_cliente.agencia = ''
                    pagina -= 1
                elif conta_cliente.agencia == 0:
                    conta_cliente.agencia = ''
                    pass
                else:
                    pagina += 1
            elif pagina == 2:
                conta_cliente.conta = cls.__obter_conta_cliente()

                if conta_cliente.conta == 1:
                    conta_cliente.conta = ''
                    conta_cliente.agencia = ''
                    pagina -= 1
                elif conta_cliente.conta == 0:
                    conta_cliente.conta = ''
                    pass
                else:
                    if Dados.verificar_conta_existe(conta_cliente):
                        pagina += 1
                    else:
                        conta_cliente.conta = ''
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'Conta não cadastrada.') 
            elif pagina == 3:
                valor = cls.__obter_valor_financeiro()
                _, _, _, __saldo = Dados.obter_informacoes_bancarias(conta_cliente.agencia, conta_cliente.conta)
        
                if valor == 1:
                    valor = ''
                    conta_cliente.conta = ''
                    pagina -= 1
                elif valor == 0:
                    valor = ''
                    pass
                else:
                    if float(valor) > float(__saldo):
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'O valor R$ "{float(valor):.2f}" é maior que seu saldo R$ "{float(__saldo):.2f}".')
                        valor = ''
                    else:
                        pagina += 1
            elif pagina == 4:
                Interfaces.imprimir_input()
                confirmacao = input()

                if Validadores.validar_opcao_menu(confirmacao, 2):
                    if int(confirmacao) == 1:
                        _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(conta_cliente.agencia, conta_cliente.conta)

                        conta_antiga = Conta(_agencia, _conta, _cpf, _saldo)
                        conta_nova = Conta(_agencia, _conta, _cpf, str(float(_saldo) - float(valor)))


                        Utilitarios.limpar_terminal()
                        Dados.editar_conta(conta_antiga, conta_nova)
                        Interfaces.imprimir_menu_mensagem_de_conclusao(f'Saque realizado com sucesso.')

                        nome = Dados.obter_informacoes_pessoais(_cpf)
                        cliente = Cliente(cpf=_cpf, nome=nome)
                        cls.__escrever_movimentacao(remetente=cliente, destinatario=cliente, acao='saque', valor=valor)

                        pagina = 0
                    else:
                        valor = ''
                        pagina -= 1
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{confirmacao}" é inválido.') 
            else:
                break


    # Transferir
    @classmethod
    def __transferir(cls):
        conta_cliente_remetente = Conta()
        conta_cliente_destinatario = Conta()

        valor = ''
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_transferir(conta_cliente_remetente.agencia, conta_cliente_remetente.conta, conta_cliente_destinatario.agencia, conta_cliente_destinatario.conta, valor)

            if pagina == 1:
                conta_cliente_remetente.agencia = cls.__obter_agencia()

                if conta_cliente_remetente.agencia == 1:
                    conta_cliente_remetente.agencia = ''
                    pagina -= 1
                elif conta_cliente_remetente.agencia == 0:
                    conta_cliente_remetente.agencia = ''
                    pass
                else:
                    pagina += 1
            elif pagina == 2:
                conta_cliente_remetente.conta = cls.__obter_conta_cliente()

                if conta_cliente_remetente.conta == 1:
                    conta_cliente_remetente.conta = ''
                    conta_cliente_remetente.agencia = ''
                    pagina -= 1
                elif conta_cliente_remetente.conta == 0:
                    conta_cliente_remetente.conta = ''
                    pass
                else:
                    if Dados.verificar_conta_existe(conta_cliente_remetente):
                        pagina += 1
                    else:
                        conta_cliente_remetente.conta = ''
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'Conta não cadastrada.') 
            elif pagina == 3:
                valor = cls.__obter_valor_financeiro()
                if valor == 1:
                    valor = ''
                    conta_cliente_remetente.conta = ''
                    pagina -= 1
                elif valor == 0:
                    valor = ''
                    pass
                else:
                    _, _, _, __saldo = Dados.obter_informacoes_bancarias(conta_cliente_remetente.agencia, conta_cliente_remetente.conta)
                    if float(valor) > float(__saldo):
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'O valor R$ "{float(valor):.2f}" é maior que seu saldo R$ "{float(__saldo):.2f}".')
                        valor = ''
                    else:
                        pagina += 1
            elif pagina == 4:
                conta_cliente_destinatario.agencia = cls.__obter_agencia()

                if conta_cliente_destinatario.agencia == 1:
                    valor = ''
                    conta_cliente_destinatario.agencia = ''
                    pagina -= 1
                elif conta_cliente_destinatario.agencia == 0:
                    conta_cliente_destinatario.agencia = ''
                    pass
                else:
                    pagina += 1
            elif pagina == 5:
                conta_cliente_destinatario.conta = cls.__obter_conta_cliente()

                if conta_cliente_destinatario.conta == 1:
                    conta_cliente_destinatario.conta = ''
                    conta_cliente_destinatario.agencia = ''
                    pagina -= 1
                elif conta_cliente_destinatario.conta == 0:
                    conta_cliente_destinatario.conta = ''
                    pass
                else:
                    if Dados.verificar_conta_existe(conta_cliente_destinatario):
                        if conta_cliente_remetente.agencia == conta_cliente_destinatario.agencia and conta_cliente_destinatario.conta == conta_cliente_remetente.conta:
                            conta_cliente_destinatario.conta = ''
                            Utilitarios.limpar_terminal()
                            Interfaces.imprimir_menu_mensagem_de_erro(f'A conta não pode ser igual.') 
                        else:
                            pagina += 1
                    else:
                        conta_cliente_destinatario.conta = ''
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'Conta não cadastrada.') 
            elif pagina == 6:
                Interfaces.imprimir_input()
                confirmacao = input()

                if Validadores.validar_opcao_menu(confirmacao, 2):
                    if int(confirmacao) == 1:
                        _agencia_remetente, _conta_remetente, _cpf_remetente, _saldo_remetente = Dados.obter_informacoes_bancarias(conta_cliente_remetente.agencia, conta_cliente_remetente.conta)
                        _agencia_destinatario, _conta_destinatario, _cpf_destinatario, _saldo_destinatario = Dados.obter_informacoes_bancarias(conta_cliente_destinatario.agencia, conta_cliente_destinatario.conta)

                        conta_antiga_remetente = Conta(_agencia_remetente, _conta_remetente, _cpf_remetente, _saldo_remetente)
                        conta_nova_remetente = Conta(_agencia_remetente, _conta_remetente, _cpf_remetente, str(float(_saldo_remetente) - float(valor)))

                        conta_antiga_destinatario = Conta(_agencia_destinatario, _conta_destinatario, _cpf_destinatario, _saldo_destinatario)
                        conta_nova_destinatario = Conta(_agencia_destinatario, _conta_destinatario, _cpf_destinatario, str(float(_saldo_destinatario) + float(valor)))
    
                        Utilitarios.limpar_terminal()
                        Dados.editar_conta(conta_antiga_remetente, conta_nova_remetente)
                        Dados.editar_conta(conta_antiga_destinatario, conta_nova_destinatario)
                        Interfaces.imprimir_menu_mensagem_de_conclusao(f'Transferência realizado com sucesso.')

                        nome_remetente = Dados.obter_informacoes_pessoais(_cpf_remetente)
                        nome_destinatario = Dados.obter_informacoes_pessoais(_cpf_destinatario)
            
                        cliente_remetente = Cliente(cpf=_cpf_remetente, nome=nome_remetente)
                        cliente_destinatario = Cliente(cpf=_agencia_destinatario, nome=nome_destinatario)

                        cls.__escrever_movimentacao(remetente=cliente_remetente, destinatario=cliente_destinatario, acao='transferencia', valor=valor)

                        pagina = 0
                    else:
                        conta_cliente_destinatario.conta = ''
                        pagina -= 1
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{confirmacao}" é inválido.') 
            else:
                break


    # Depositar
    @classmethod
    def __depositar(cls):
        conta_cliente = Conta()
        valor = ''
        pagina = 1

        while pagina > 0:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_depositar(conta_cliente.agencia, conta_cliente.conta, valor)

            if pagina == 1:
                conta_cliente.agencia = cls.__obter_agencia()

                if conta_cliente.agencia == 1:
                    conta_cliente.agencia = ''
                    pagina -= 1
                elif conta_cliente.agencia == 0:
                    conta_cliente.agencia = ''
                    pass
                else:
                    pagina += 1
            elif pagina == 2:
                conta_cliente.conta = cls.__obter_conta_cliente()

                if conta_cliente.conta == 1:
                    conta_cliente.conta = ''
                    conta_cliente.agencia = ''
                    pagina -= 1
                elif conta_cliente.conta == 0:
                    conta_cliente.conta = ''
                    pass
                else:
                    if Dados.verificar_conta_existe(conta_cliente):
                        pagina += 1
                    else:
                        conta_cliente.conta = ''
                        Utilitarios.limpar_terminal()
                        Interfaces.imprimir_menu_mensagem_de_erro(f'Conta não cadastrada.') 
            elif pagina == 3:
                valor = cls.__obter_valor_financeiro()

                if valor == 1:
                    valor = ''
                    conta_cliente.conta = ''
                    pagina -= 1
                elif valor == 0:
                    valor = ''
                    pass
                else:
                    pagina += 1
            elif pagina == 4:
                Interfaces.imprimir_input()
                confirmacao = input()

                if Validadores.validar_opcao_menu(confirmacao, 2):
                    if int(confirmacao) == 1:
                        _agencia, _conta, _cpf, _saldo = Dados.obter_informacoes_bancarias(conta_cliente.agencia, conta_cliente.conta)

                        conta_antiga = Conta(_agencia, _conta, _cpf, _saldo)
                        conta_nova = Conta(_agencia, _conta, _cpf, str(float(_saldo) + float(valor)))


                        Utilitarios.limpar_terminal()
                        Dados.editar_conta(conta_antiga, conta_nova)
                        Interfaces.imprimir_menu_mensagem_de_conclusao(f'Depósito realizado com sucesso.')

                        nome = Dados.obter_informacoes_pessoais(_cpf)
                        cliente = Cliente(cpf=_cpf, nome=nome)
                        cls.__escrever_movimentacao(remetente=cliente, destinatario=cliente, acao='deposito', valor=valor)

                        pagina = 0
                    else:
                        valor = ''
                        pagina -= 1
                else:
                    Utilitarios.limpar_terminal()
                    Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{confirmacao}" é inválido.') 
            else:
                break


    @staticmethod
    def __escrever_movimentacao(remetente : Cliente, destinatario : Cliente, acao, valor, data=''):
        if data == '':
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
        else:
            pass
        movimentacao = Movimentacao(remetente=remetente, destinatario=destinatario, acao=acao, valor=valor, data=data)
        Dados.add_movimentacao(movimentacao)


    @staticmethod
    def __obter_valor_financeiro():
        rprint('[bright_cyan bold]| -> [/]', end=''); valor = input().strip()

        if valor == '1':
            return 1
        else:
            if Validadores.validar_valor_financeiro(valor):
                return valor
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{valor}" é inválido.')
                return 0


    @staticmethod
    def __obter_conta_cliente():
        rprint('[bright_cyan bold]| -> [/]', end=''); numero_conta = input().strip()

        if numero_conta == '1':
            return 1
        else:
            if Validadores.validar_numero_da_conta(numero_conta):
                return numero_conta
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{numero_conta}" é inválido.')
                return 0         


    @staticmethod
    def __obter_agencia():
        rprint('[bright_cyan bold]| -> [/]', end=''); numero_agencia = input().strip()

        if numero_agencia == '1':
            return 1
        else:
            if Validadores.validar_numero_da_agencia(numero_agencia):
                return numero_agencia
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{numero_agencia}" é inválido.')
                return 0


    # Menu sair
    @classmethod
    def __menu_sair(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_sair()
            Interfaces.imprimir_input()
            opcao_usuario_menu_sair = input().strip()

            if Validadores.validar_opcao_menu(opcao_usuario_menu_sair, 3):
                if int(opcao_usuario_menu_sair) == 3:
                    break
                else:
                    cls.__opcoes_menu_sair(int(opcao_usuario_menu_sair))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_sair}" é inválido.')


    @classmethod
    def __opcoes_menu_sair(cls, opcao_usuario_menu_sair : int):
        if opcao_usuario_menu_sair == 1:
            cls.__menu_salvar_e_sair()
        elif opcao_usuario_menu_sair == 2:
            cls.__menu_sair_sem_salvar()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_usuario_menu_sair}" é inválido.')
    
    # Salvar e sair
    @classmethod
    def __menu_salvar_e_sair(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_confirmacao()
            Interfaces.imprimir_input()
            opcao_menu_salvar_e_sair = input().strip()

            if Validadores.validar_opcao_menu(opcao_menu_salvar_e_sair, 2):
                if int(opcao_menu_salvar_e_sair) == 2:
                    break
                else:
                    cls.__opcoes_menu_salvar_e_sair(int(opcao_menu_salvar_e_sair))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_menu_salvar_e_sair}" é inválido.')


    @classmethod
    def __opcoes_menu_salvar_e_sair(cls, opcao_menu_salvar_e_sair : int):
        if opcao_menu_salvar_e_sair == 1:
            cls.__salvar_e_sair()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_menu_salvar_e_sair}" é inválido.')


    @classmethod
    def __salvar_e_sair(cls):
        cls.__salvar_arquivos()
        Utilitarios.limpar_terminal()
        Interfaces.imprimir_menu_mensagem_de_conclusao('Download realizado com sucesso.')

        Utilitarios.limpar_terminal()
        cls.sair()


    @staticmethod
    def sair():
        exit()


    @staticmethod
    def __salvar_arquivos():
        zip = zipfile.ZipFile('dados.zip', 'w', zipfile.ZIP_DEFLATED)
        zip.write('..\sistema\src\dados\clientes.csv')
        zip.write('..\sistema\src\dados\contas.csv')
        zip.write('..\sistema\src\dados\movimentacoes.csv')
        zip.close()


    # Sair
    @classmethod
    def __menu_sair_sem_salvar(cls):
        while True:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_confirmacao()
            Interfaces.imprimir_input()
            opcao_menu_sair_sem_salvar = input().strip()

            if Validadores.validar_opcao_menu(opcao_menu_sair_sem_salvar, 2):
                if int(opcao_menu_sair_sem_salvar) == 2:
                    break
                else:
                    cls.__opcoes_menu_sair_sem_salvar(int(opcao_menu_sair_sem_salvar))
            else:
                Utilitarios.limpar_terminal()
                Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_menu_sair_sem_salvar}" é inválido.')


    @classmethod
    def __opcoes_menu_sair_sem_salvar(cls, opcao_menu_sair_sem_salvar : int):
        if opcao_menu_sair_sem_salvar == 1:
            cls.__sair_sem_salvar()
        else:
            Utilitarios.limpar_terminal()
            Interfaces.imprimir_menu_mensagem_de_erro(f'O valor "{opcao_menu_sair_sem_salvar}" é inválido.')


    @classmethod
    def __sair_sem_salvar(cls):
        Utilitarios.limpar_terminal()
        cls.sair()
