'''
Classe resposável pela criação da conta
'''


class Conta:
    def __init__(
            self,
            agencia: str = '',
            conta: str = '',
            cpf: str = '',
            saldo: str = '') -> None:
        self.__agencia = agencia
        self.__conta = conta
        self.__cpf = cpf
        self.__saldo = saldo


    # Seção getters
    @property
    def agencia(self) -> str:
        return self.__agencia


    @property
    def conta(self) -> str:
        return self.__conta


    @property
    def cpf(self) -> str:
        return self.__cpf


    @property
    def saldo(self) -> str:
        return self.__saldo


    # Seção setters
    @saldo.setter
    def saldo(self, saldo: str) -> None:
        self.__saldo = saldo


    @agencia.setter
    def agencia(self, agencia: str) -> None:
        self.__agencia = agencia


    @conta.setter
    def conta(self, conta: str) -> None:
        self.__conta = conta


    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self.__cpf = cpf
