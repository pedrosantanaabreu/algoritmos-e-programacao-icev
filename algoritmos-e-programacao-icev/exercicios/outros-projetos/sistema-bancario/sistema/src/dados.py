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


# Path
path_clientes = '..\sistema\src\dados\clientes.csv'
path_contas = '..\sistema\src\dados\contas.csv'
path_movimentacoes = '..\sistema\src\dados\movimentacoes.csv'


class Dados:
    # Seção adicionar
    @staticmethod
    def adicionar_cliente_no_banco_de_dados(cliente: Cliente) -> None:
        try:
            with open(path_clientes, 'r+', encoding='utf-8', newline='') as clientes_csv_leitura:
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


    @staticmethod
    def adicionar_conta_no_banco_de_dados(conta: Conta) -> None:
        try:
            with open(path_contas, 'r+', encoding='utf-8', newline='') as contas_csv_leitura:
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


    @staticmethod
    def adicionar_movimentacao_no_banco_de_dados(movimentacao: Movimentacao) -> None:
        try:
            with open(path_movimentacoes, 'r+', encoding='utf-8', newline='') as movimentacao_csv_leitura:
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
    @staticmethod
    def deletar_cliente_no_banco_de_dados(cliente: Cliente) -> None:
        try:
            # Salvando o arquivo em uma lista e excluindo o cliente da lista
            with open(path_clientes, 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
                clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

                linhas_banco_de_dados_clientes = list(clientes_csv_leitura)
                linhas_banco_de_dados_clientes.remove(
                    [
                        cliente.nome,
                        cliente.cpf
                    ]
                )

            # Escrevendo a lista no arquivo sem o cliente
            with open(path_clientes, 'w') as clientes_csv_escrita:
                clientes_csv_escrita = csv.writer(clientes_csv_escrita)
                clientes_csv_escrita.writerows(linhas_banco_de_dados_clientes)
        except:
            pass


    @staticmethod
    def deletar_conta_no_banco_de_dados(conta: Conta) -> None:
        try:
            # Salvando o arquivo em uma lista e excluindo a conta da lista
            with open(path_contas, 'r', encoding='utf-8', newline='') as contas_csv_leitura:
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
            with open(path_contas, 'w') as contas_csv_escrita:
                contas_csv_escrita = csv.writer(contas_csv_escrita)
                contas_csv_escrita.writerows(linhas_banco_de_dados_contas)
        except:
            pass
    
    
    @staticmethod
    def deletar_movimentacao_do_banco_de_dados(movimentacao: Movimentacao) -> None:
        try:
            # Salvando o arquivo em uma lista e excluindo a movimentação da lista
            with open(path_movimentacoes, 'r', encoding='utf-8', newline='') as movimentacoes_csv_leitura:
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
            with open(path_movimentacoes, 'w') as movimentacoes_csv_leitura:
                movimentacoes_csv_leitura = csv.writer(movimentacoes_csv_leitura)
                movimentacoes_csv_leitura.writerows(linhas_banco_de_dados_movimentacoes)
        except:
            pass
    

    # Seção obter dados
    @staticmethod
    def obter_informacoes_bancarias_por_agencia_ou_cpf(agencia: str = '', conta: str = '', cpf: str = '') -> list:
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
                with open(path_contas, 'r', encoding='utf-8', newline='') as contas_csv_leitura:
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
            with open(path_contas, 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
                
                for linhas_banco_de_dados_contas in contas_csv_leitura:
                    try:
                        agencia_e_conta_banco_de_dados = str(linhas_banco_de_dados_contas[0]) + str(linhas_banco_de_dados_contas[1])
                        agencia_e_conta_cliente = str(agencia) + str(conta)
        
                        if agencia_e_conta_banco_de_dados == agencia_e_conta_cliente:
                            return linhas_banco_de_dados_contas
                    except:
                        pass


    @staticmethod
    def obter_informacoes_pessoais_por_cpf(cpf: str) -> str:
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
            with open(path_clientes, 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
                clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

                for linha in clientes_csv_leitura:
                    try:
                        if cpf == linha[1]:
                            return linha[0]
                    except:
                        pass
        except:
            pass


    @staticmethod
    def obter_lista_de_movimentacoes() -> list:
        try:
            with open(path_movimentacoes, 'r', encoding='utf-8', newline='') as movimentacoes_csv_leitura:
                movimentacoes_csv_leitura = csv.reader(movimentacoes_csv_leitura, delimiter=',')

                linhas_banco_de_dados_movimentacoes = list(movimentacoes_csv_leitura)
                return linhas_banco_de_dados_movimentacoes
        except:
            pass


    @staticmethod
    def obter_lista_de_contas() -> list:
        try:
            with open(path_contas, 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')

                linhas_banco_de_dados_contas = list(contas_csv_leitura)
                return linhas_banco_de_dados_contas
        except:
            pass


    @staticmethod
    def obter_lista_de_clientes() -> list:
        with open(path_clientes, 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

            linhas_banco_de_dados_clientes = list(clientes_csv_leitura)
            return linhas_banco_de_dados_clientes


    # Verificar
    @staticmethod
    def verificar_se_cliente_existe(cliente: Cliente) -> bool:
        with open(path_clientes, 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            if cliente.cpf in clientes_csv_leitura.read():
                return True
            else:
                return False


    @staticmethod
    def verificar_se_conta_existe(conta: Conta) -> bool:
        try:
            with open(path_contas, 'r', encoding='utf-8', newline='') as contas_csv_leitura:
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


    @staticmethod
    def verificar_cpf_cadastrado_em_conta(cpf: str) -> bool:
        try:
            with open(path_contas, 'r', encoding='utf-8', newline='') as contas_csv_leitura:
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
    @staticmethod
    def deletar_linhas_em_branco(banco_de_dados: str) -> None:
        banco_de_dados_path = {
            'clientes': path_clientes,
            'movimentacoes': path_movimentacoes,
            'contas' : path_contas
        }

        try:
            with open(banco_de_dados_path[banco_de_dados], 'r') as arquivo_leitura:
                linhas_banco_de_dados = arquivo_leitura.readlines()


            with open(banco_de_dados_path[banco_de_dados], 'w') as arquivo_escrita:
                for linha in linhas_banco_de_dados:
                    if linha == '\n':
                        pass
                    else:
                        arquivo_escrita.write(linha)
        except:
            pass
