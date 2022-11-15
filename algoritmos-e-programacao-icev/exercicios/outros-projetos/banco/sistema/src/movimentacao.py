from .cliente import Cliente


class Movimentacao:
    def __init__(self, remetente : Cliente, destinatario : Cliente, acao : str, valor : float, data : str):
        self.__remetente = remetente.nome
        self.__destinatario = destinatario.nome
        self.__acao = acao
        self.__valor = valor
        self.__data = data


    @property
    def remetente(self):
        return self.__remetente


    @property
    def data(self):
        return self.__data


    @property
    def destinatario(self):
        return self.__destinatario


    @property
    def acao(self):
        return self.__acao

    @property
    def valor(self):
        return self.__valor


    @remetente.setter
    def saldo(self, remetente : Cliente):
        self.__remetente = remetente.nome


    @data.setter
    def saldo(self, data):
        self.__remetente = data


    @destinatario.setter
    def agencia(self, destinatario : Cliente):
        self.__destinatario = destinatario.nome


    @acao.setter
    def conta(self, acao : str):
        self.__acao = acao


    @valor.setter
    def valor(self, valor : float):
        self.__valor = valor
