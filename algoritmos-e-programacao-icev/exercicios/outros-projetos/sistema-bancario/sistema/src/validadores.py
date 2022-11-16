'''
Classe responsável por validar as informações
'''


# Módulos internos
from .utilitarios import Utilitarios


class Validadores:
    # Validadores
    @staticmethod
    def validar_opcao_menu(opcao_usuario: str, opcoes_menu: int) -> bool:
        try:
            opcao_usuario = int(opcao_usuario)
            if opcao_usuario in list(range(1, opcoes_menu + 1)):
                return True
            else:
                return False
        except:
            return False


    @staticmethod
    def validar_nome(nome: str) -> bool:
        try:
            if Utilitarios.formatar_string(nome).isalpha():
                return True
            else:
                return False
        except:
            return False


    @classmethod
    def validar_cpf(cls, cpf: str) -> bool:
        cpf = Utilitarios.formatar_cpf(cpf)

        if len(cpf) == 11:
            try:
                primeiro_digito_verificador = int(cpf[-2])
                segundo_digito_verificador = int(cpf[-1])

                calculo_primeiro_digito = cls.obter_digitos_verificadores(cpf[0:9])
                calculo_segundo_digito = cls.obter_digitos_verificadores(cpf[1:10])
            except:
                pass

            if (calculo_primeiro_digito == primeiro_digito_verificador and calculo_segundo_digito == segundo_digito_verificador):
                return True
            else:
                return False
        else:
            return False


    @staticmethod
    def validar_numero_da_agencia(agencia: str) -> bool:
        try:
            if (Utilitarios.formatar_numero(agencia).isnumeric() and len(Utilitarios.formatar_numero(agencia)) == 4):
                return True
            else:
                return False
        except:
            return False


    @staticmethod
    def validar_numero_da_conta(conta: str) -> bool:
        try:
            if (Utilitarios.formatar_numero(conta).isnumeric() and len(Utilitarios.formatar_numero(conta)) == 9):
                return True
            else:
                return False
        except:
            return False


    @staticmethod
    def validar_valor_financeiro(valor: str) -> bool:
        try:
            float(valor)
            if float(valor) >= 0:
                return True
            else:
                return False
        except:
            return False


    # Obter
    @staticmethod
    def obter_digitos_verificadores(numeros: str) -> int:
        resultado_soma_digitos = 0

        for index, multiplicador in enumerate(numeros):
            resultado_soma_digitos += (10 - index) * int(multiplicador)

        if resultado_soma_digitos % 11 <= 1:
            digito_final = 0
        else:
            digito_final = 11 - resultado_soma_digitos % 11

        return digito_final
