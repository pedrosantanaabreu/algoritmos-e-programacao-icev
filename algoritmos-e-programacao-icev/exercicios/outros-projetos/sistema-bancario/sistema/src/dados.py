'''
Classe resposável pela interação com o banco de dados
'''


# Módulos internos
from .cliente import Cliente
from .conta import Conta
from .movimentacao import Movimentacao
from .utilitarios import Utilitarios


# Módulos externos
import csv


class Dados:
    # Path
    __path = {
        'clientes': '..\sistema\src\dados\clientes.csv',
        'contas': '..\sistema\src\dados\contas.csv',
        'movimentacoes': '..\sistema\src\dados\movimentacoes.csv' 
    }

    
    # Seção adicionar
    @classmethod
    def adicionar_cliente_no_banco_de_dados(cls, cliente: Cliente) -> None:
        try:
            with open(cls.__path['clientes'], 'r+', encoding='utf-8', newline='') as clientes_csv_leitura:
                clientes_csv_escrita = csv.writer(clientes_csv_leitura)

                # Se o arquivo estiver vazio, será criado os cabeçalhos
                if not bool(clientes_csv_leitura.readlines()):
                    clientes_csv_escrita.writerow(
                        [
                            'nome',
                            'cpf'
                        ]
                    )
                else:
                    clientes_csv_escrita.writerow(
                        [
                            Utilitarios.formatar_nome(cliente.nome),
                            Utilitarios.formatar_cpf(cliente.cpf)
                        ]
                    )
        except:
            pass


    @classmethod
    def adicionar_conta_no_banco_de_dados(cls, conta: Conta) -> None:
        try:
            with open(cls.__path['contas'], 'r+', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_escrita = csv.writer(contas_csv_leitura)
                
                # Se o arquivo estiver vazio, será criado os cabeçalhos
                if not bool(contas_csv_leitura.readlines()):
                    contas_csv_escrita.writerow(
                        [
                            'agencia',
                            'conta',
                            'cpf',
                            'saldo'
                        ]
                    )
                else:
                    contas_csv_escrita.writerow(
                        [
                            Utilitarios.formatar_numero(conta.agencia),
                            Utilitarios.formatar_numero(conta.conta),
                            Utilitarios.formatar_cpf(conta.cpf),
                            Utilitarios.formatar_dinheiro(conta.saldo),
                        ]
                    )
        except:
            pass


    @classmethod
    def adicionar_movimentacao_no_banco_de_dados(cls, movimentacao: Movimentacao) -> None:
        try:
            with open(cls.__path['movimentacoes'], 'r+', encoding='utf-8', newline='') as movimentacao_csv_leitura:
                movimentacao_csv_escrita = csv.writer(movimentacao_csv_leitura)

                # Se o arquivo estiver vazio, será criado os cabeçalhos
                if not bool(movimentacao_csv_leitura.readlines()):
                    movimentacao_csv_escrita.writerow(
                        [
                            'remetente',
                            'destinatario',
                            'acao',
                            'valor',
                            'data'
                        ]
                    )
                else:
                    movimentacao_csv_escrita.writerow(
                        [
                            Utilitarios.formatar_nome(movimentacao.remetente),
                            Utilitarios.formatar_nome(movimentacao.destinatario),
                            Utilitarios.formatar_nome(movimentacao.acao),
                            Utilitarios.formatar_dinheiro(movimentacao.valor),
                            movimentacao.data,
                        ]
                    )
        except:
            pass


    # Seção deletar
    @classmethod
    def deletar_cliente_no_banco_de_dados(cls, cliente: Cliente) -> None:
        try:
            # Salvando o arquivo em uma lista e excluindo o cliente da lista
            with open(cls.__path['clientes'], 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
                clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

                linhas_banco_de_dados_clientes = list(clientes_csv_leitura)
                linhas_banco_de_dados_clientes.remove(
                    [
                        cliente.nome,
                        cliente.cpf
                    ]
                )

            # Escrevendo a lista no arquivo sem o cliente
            with open(cls.__path['clientes'], 'w') as clientes_csv_escrita:
                clientes_csv_escrita = csv.writer(clientes_csv_escrita)
                clientes_csv_escrita.writerows(linhas_banco_de_dados_clientes)
        except:
            pass


    @classmethod
    def deletar_conta_no_banco_de_dados(cls, conta: Conta) -> None:
        try:
            # Salvando o arquivo em uma lista e excluindo a conta da lista
            with open(cls.__path['contas'], 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
                
                linhas_banco_de_dados_contas = list(contas_csv_leitura)
                linhas_banco_de_dados_contas.remove(
                    [
                        conta.agencia,
                        conta.conta,
                        conta.cpf,
                        conta.saldo
                    ]
                )

            # Escrevendo a lista no arquivo sem a conta
            with open(cls.__path['contas'], 'w') as contas_csv_escrita:
                contas_csv_escrita = csv.writer(contas_csv_escrita)
                contas_csv_escrita.writerows(linhas_banco_de_dados_contas)
        except:
            pass
    
    
    @classmethod
    def deletar_movimentacao_do_banco_de_dados(cls, movimentacao: Movimentacao) -> None:
        try:
            # Salvando o arquivo em uma lista e excluindo a movimentação da lista
            with open(cls.__path['movimentacoes'], 'r', encoding='utf-8', newline='') as movimentacoes_csv_leitura:
                movimentacoes_csv_leitura = csv.reader(movimentacoes_csv_leitura, delimiter=',')
    
                linhas_banco_de_dados_movimentacoes = list(movimentacoes_csv_leitura)
                linhas_banco_de_dados_movimentacoes.remove(
                    [
                        movimentacao.remetente,
                        movimentacao.destinatario,
                        movimentacao.acao,
                        movimentacao.valor,
                        movimentacao.data
                    ]
                )
                
            # Escrevendo a lista no arquivo sem a movimentação
            with open(cls.__path['movimentacoes'], 'w') as movimentacoes_csv_leitura:
                movimentacoes_csv_leitura = csv.writer(movimentacoes_csv_leitura)
                movimentacoes_csv_leitura.writerows(linhas_banco_de_dados_movimentacoes)
        except:
            pass
    

    # Seção obter dados
    @classmethod
    def obter_informacoes_bancarias_por_agencia_ou_cpf(cls, agencia: str = '', conta: str = '', cpf: str = '') -> list:
        '''
        Função resposável por enviar informações bancárias
            [
                agencia,
                conta,
                cpf,
                saldo
            ]
        Recebe ou o CPF ou agência e conta

        Argumentos:
            agencia (str, opcional): será utilizado a busca por conta. Predefinição ''.
            conta (str, opcional): será utilizado a busca por conta. Predefinição ''.
            cpf (str, opcional): será utilizado a busca por CPF. Predefinição ''.

        Retorno:
            list : [agencia, conta, cpf, saldo]
        '''
        
        
        # Se o CPF for diferente de '' será usado a busca por CPF
        if cpf != '':
            try:
                with open(cls.__path['contas'], 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                    contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')

                    for linhas_banco_de_dados_contas in contas_csv_leitura:
                        try:
                            if cpf == linhas_banco_de_dados_contas[2]:
                                return linhas_banco_de_dados_contas
                        except:
                            pass
            except:
                pass

        # Caso contrário, significa que será utilizado a busca por agência e conta
        else:
            with open(cls.__path['contas'], 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
                
                for linhas_banco_de_dados_contas in contas_csv_leitura:
                    try:
                        agencia_e_conta_banco_de_dados = str(linhas_banco_de_dados_contas[0]) + str(linhas_banco_de_dados_contas[1])
                        agencia_e_conta_cliente = str(agencia) + str(conta)
        
                        if agencia_e_conta_banco_de_dados == agencia_e_conta_cliente:
                            return linhas_banco_de_dados_contas
                    except:
                        pass


    @classmethod
    def obter_informacoes_pessoais_por_cpf(cls, cpf: str) -> str:
        '''
        Função resposável por enviar informações pessoais
            [
                cpf,
            ]
        Recebe CPF

        Argumentos:
            cpf (str, opcional): será utilizado a busca por cliente.

        Retorno:
            str : nome
        '''


        try:
            with open(cls.__path['clientes'], 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
                clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

                for linha in clientes_csv_leitura:
                    try:
                        if cpf == linha[1]:
                            return linha[0]
                    except:
                        pass
        except:
            pass


    @classmethod
    def obter_lista_de_movimentacoes(cls) -> list:
        try:
            with open(cls.__path['movimentacoes'], 'r', encoding='utf-8', newline='') as movimentacoes_csv_leitura:
                movimentacoes_csv_leitura = csv.reader(movimentacoes_csv_leitura, delimiter=',')

                linhas_banco_de_dados_movimentacoes = list(movimentacoes_csv_leitura)
                return linhas_banco_de_dados_movimentacoes
        except:
            pass


    @classmethod
    def obter_lista_de_contas(cls) -> list:
        try:
            with open(cls.__path['contas'], 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')

                linhas_banco_de_dados_contas = list(contas_csv_leitura)
                return linhas_banco_de_dados_contas
        except:
            pass


    @classmethod
    def obter_lista_de_clientes(cls) -> list:
        with open(cls.__path['clientes'], 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

            linhas_banco_de_dados_clientes = list(clientes_csv_leitura)
            return linhas_banco_de_dados_clientes


    # Verificar
    @classmethod
    def verificar_se_cliente_existe(cls, cliente: Cliente) -> bool:
        with open(cls.__path['clientes'], 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            if cliente.cpf in clientes_csv_leitura.read():
                return True
            else:
                return False


    @classmethod
    def verificar_se_conta_existe(cls, conta: Conta) -> bool:
        try:
            with open(cls.__path['contas'], 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
        
                for linhas_banco_de_dados_contas in contas_csv_leitura:
                    try:
                        agencia_e_conta_banco_de_dados = str(linhas_banco_de_dados_contas[0]) + str(linhas_banco_de_dados_contas[1])
                        agencia_e_conta_cliente = str(conta.agencia) + str(conta.conta)

                        if agencia_e_conta_banco_de_dados == agencia_e_conta_cliente:
                            return True
                    except:
                        pass
                return False
        except:
            pass


    @classmethod
    def verificar_cpf_cadastrado_em_conta(cls, cpf: str) -> bool:
        try:
            with open(cls.__path['contas'], 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')

                for linhas_banco_de_dados_contas in contas_csv_leitura:
                    try:
                        if str(linhas_banco_de_dados_contas[2]).strip() == cpf:
                            return True
                    except:
                        pass
                return False
        except:
            pass


    # Editar
    @classmethod
    def editar_cliente(cls, cliente_antigo: Cliente, cliente_novo: Cliente) -> None:
        cls.deletar_cliente_no_banco_de_dados(cliente_antigo)
        cls.adicionar_cliente_no_banco_de_dados(cliente_novo)


    @classmethod
    def editar_conta(cls, conta_antiga: Conta, conta_nova: Conta) -> None:
        cls.deletar_conta_no_banco_de_dados(conta_antiga)
        cls.adicionar_conta_no_banco_de_dados(conta_nova)


    # Outros
    @classmethod
    def deletar_linhas_em_branco(cls, banco_de_dados: str) -> None:
        try:
            with open(cls.__path[banco_de_dados], 'r') as arquivo_leitura:
                linhas_banco_de_dados = arquivo_leitura.readlines()


            with open(cls.__path[banco_de_dados], 'w') as arquivo_escrita:
                for linha in linhas_banco_de_dados:
                    if linha == '\n':
                        pass
                    else:
                        arquivo_escrita.write(linha)
        except:
            pass
