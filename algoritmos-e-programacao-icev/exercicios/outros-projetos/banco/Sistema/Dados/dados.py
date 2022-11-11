import csv


class Dados:
    @staticmethod
    def adicionar_cliente(cliente):
        with open('Sistema\Dados\Dados\clientes.csv', 'r+', encoding='utf-8', newline='', ) as arquivo:
            escrever = csv.writer(arquivo)
            if not bool(arquivo.readlines()):
                escrever.writerow(["nome", "cpf"])
            escrever.writerow([cliente['nome'], cliente['cpf']])
    

    @staticmethod
    def adicionar_conta(conta):
        with open('Sistema\Dados\Dados\contas.csv', 'r+', encoding='utf-8', newline='', ) as arquivo:
            escrever = csv.writer(arquivo)
            if not bool(arquivo.readlines()):
                escrever.writerow(["agencia", 'conta' "cpf"])
            escrever.writerow([conta['agencia'], conta['conta'], conta['cpf']])
