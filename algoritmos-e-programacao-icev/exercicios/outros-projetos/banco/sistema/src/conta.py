class Conta:
    def __init__(self, agencia : str = '', conta : str = '', cpf : str = '', saldo : str = ''):
        self.__agencia = agencia
        self.__conta = conta
        self.__cpf = cpf
        self.__saldo = saldo
    

    @property
    def agencia(self):
        return self.__agencia


    @property
    def conta(self):
        return self.__conta


    @property
    def cpf(self):
        return self.__cpf

    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, saldo : str):
        self.__saldo = saldo


    @agencia.setter
    def agencia(self, agencia : str):
        self.__agencia = agencia


    @conta.setter
    def conta(self, conta : str):
        self.__conta = conta


    @cpf.setter
    def cpf(self, cpf : str):
        self.__cpf = cpf
