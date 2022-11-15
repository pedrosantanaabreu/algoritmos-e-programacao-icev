from .cliente import Cliente
from .conta import Conta
from .movimentacao import Movimentacao
import csv


class Dados:
    # Add
    @staticmethod
    def add_cliente(cliente : Cliente):
        with open('..\sistema\src\dados\clientes.csv', 'r+', encoding='utf-8', newline='') as clientes_csv_leitura:
            clientes_csv_escrita = csv.writer(clientes_csv_leitura)
            if not bool(clientes_csv_leitura.readlines()):
                clientes_csv_escrita.writerow(["nome", "cpf"])
            else:
                clientes_csv_escrita.writerow([cliente.nome, cliente.cpf])


    @staticmethod
    def add_conta(conta : Conta):
        with open('..\sistema\src\dados\contas.csv', 'r+', encoding='utf-8', newline='') as contas_csv_leitura:
            contas_csv_escrita = csv.writer(contas_csv_leitura)
            if not bool(contas_csv_leitura.readlines()):
                contas_csv_escrita.writerow(["agencia", 'conta', "cpf", 'saldo'])
            else:
                contas_csv_escrita.writerow([conta.agencia, conta.conta, conta.cpf, conta.saldo])


    @staticmethod
    def add_movimentacao(movimentacao : Movimentacao):
        with open('..\sistema\src\dados\movimentacoes.csv', 'r+', encoding='utf-8', newline='') as movimentacao_csv_leitura:
            movimentacao_csv_escrita = csv.writer(movimentacao_csv_leitura)
            if not bool(movimentacao_csv_leitura.readlines()):
                movimentacao_csv_escrita.writerow(['remetente', 'destinatario', 'acao', 'valor', 'data'])
            else:
                movimentacao_csv_escrita.writerow([movimentacao.remetente, movimentacao.destinatario, movimentacao.acao, movimentacao.valor, movimentacao.data])


    # Del
    @staticmethod
    def del_cliente(cliente : Cliente):
        with open('..\sistema\src\dados\clientes.csv', 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')
            linhas = list(clientes_csv_leitura)
            linhas.remove([cliente.nome, cliente.cpf])

        with open('..\sistema\src\dados\clientes.csv', 'w') as clientes_csv_escrita: 
            clientes_csv_escrita = csv.writer(clientes_csv_escrita)
            clientes_csv_escrita.writerows(linhas)


    @staticmethod
    def del_conta(conta : Conta):
        with open('..\sistema\src\dados\contas.csv', 'r', encoding='utf-8', newline='') as contas_csv_leitura:
            contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
            linhas = list(contas_csv_leitura)
            linhas.remove([conta.agencia, conta.conta, conta.cpf, conta.saldo])

        with open('..\sistema\src\dados\contas.csv', 'w') as contas_csv_escrita: 
            contas_csv_escrita = csv.writer(contas_csv_escrita)
            contas_csv_escrita.writerows(linhas)


    @staticmethod
    def del_movimentacao(movimentacao : Movimentacao):
        with open('..\sistema\src\dados\movimentacoes.csv', 'r', encoding='utf-8', newline='') as movimentacoes_csv_leitura:
            movimentacoes_csv_leitura = csv.reader(movimentacoes_csv_leitura, delimiter=',')
            linhas = list(movimentacoes_csv_leitura)
            linhas.remove([movimentacao.remetente, movimentacao.destinatario, movimentacao.acao, movimentacao.valor])

        with open('..\sistema\src\dados\movimentacoes.csv', 'w') as movimentacoes_csv_leitura: 
            movimentacoes_csv_leitura = csv.writer(movimentacoes_csv_leitura)
            movimentacoes_csv_leitura.writerows(linhas)


    # Get
    @staticmethod
    def obter_informacoes_bancarias(agencia : str = '', conta : str = '', cpf : str =''):
        if cpf != '':
            with open('..\sistema\src\dados\contas.csv', 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
                for linha in contas_csv_leitura:
                    try:
                        if cpf == linha[2]:
                            return linha
                    except:
                        pass
        else:
            with open('..\sistema\src\dados\contas.csv', 'r', encoding='utf-8', newline='') as contas_csv_leitura:
                contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
                for linha in contas_csv_leitura:
                    try:
                        if str(linha[0]).strip() + str(linha[1]).strip() == str(agencia) + str(conta):
                            return linha
                    except:
                        pass


    @staticmethod
    def obter_informacoes_pessoais(cpf : str):
        with open('..\sistema\src\dados\clientes.csv', 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')

            for linha in clientes_csv_leitura:
                try:
                    if cpf == linha[1]:
                        return linha[0]
                except:
                    pass


    @staticmethod
    def obter_lista_de_movimentacoes():
        with open('..\sistema\src\dados\movimentacoes.csv', 'r', encoding='utf-8', newline='') as movimentacoes_csv_leitura:
            movimentacoes_csv_leitura = csv.reader(movimentacoes_csv_leitura, delimiter=',')
            linhas = list(movimentacoes_csv_leitura)
            return linhas


    @staticmethod
    def obter_lista_de_contas():
        with open('..\sistema\src\dados\contas.csv', 'r', encoding='utf-8', newline='') as contas_csv_leitura:
            contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
            linhas = list(contas_csv_leitura)
            return linhas


    @staticmethod
    def obter_lista_de_clientes():
        with open('..\sistema\src\dados\clientes.csv', 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            clientes_csv_leitura = csv.reader(clientes_csv_leitura, delimiter=',')
            linhas = list(clientes_csv_leitura)
            return linhas


    # Verificar
    @staticmethod
    def verificar_cliente_existe(cliente : Cliente):
        with open('..\sistema\src\dados\clientes.csv', 'r', encoding='utf-8', newline='') as clientes_csv_leitura:
            if cliente.cpf in clientes_csv_leitura.read():
                return True
            else:
                return False


    @staticmethod
    def verificar_conta_existe(conta : Conta):
        with open('..\sistema\src\dados\contas.csv', 'r', encoding='utf-8', newline='') as contas_csv_leitura:
            contas_csv_leitura = csv.reader(contas_csv_leitura, delimiter=',')
            for linha in contas_csv_leitura:
                try:
                    if str(linha[0]).strip() + str(linha[1]).strip() == str(conta.agencia) + str(conta.conta):
                        return True
                except:
                    pass
            return False


    # Editar
    @classmethod
    def editar_cliente(cls, cliente_antigo : Cliente, cliente_novo : Cliente):
        cls.del_cliente(cliente_antigo)
        cls.add_cliente(cliente_novo)


    @classmethod
    def editar_conta(cls, conta_antiga : Conta, conta_nova : Conta):
        cls.del_conta(conta_antiga)
        cls.add_conta(conta_nova)
