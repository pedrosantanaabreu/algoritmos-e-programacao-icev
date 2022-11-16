# Módulos internos
from .cliente import Cliente


class Movimentacao:
    def __init__(
            self,
            remetente: Cliente = Cliente(),
            destinatario: Cliente = Cliente(),
            acao: str = '',
            valor: str = '',
            data: str = '',
        ) -> None:
        self.__remetente = remetente.nome
        self.__destinatario = destinatario.nome
        self.__acao = acao
        self.__valor = valor
        self.__data = data


    # Seção getters
    @property
    def remetente(self) -> str:
        return self.__remetente


    @property
    def data(self) -> str:
        return self.__data


    @property
    def destinatario(self) -> str:
        return self.__destinatario


    @property
    def acao(self) -> str:
        return self.__acao


    @property
    def valor(self) -> str:
        return self.__valor


    # Seção setters
    @remetente.setter
    def saldo(self, remetente: Cliente) -> None:
        self.__remetente = remetente.nome


    @data.setter
    def saldo(self, data) -> None:
        self.__remetente = data


    @destinatario.setter
    def agencia(self, destinatario: Cliente) -> None:
        self.__destinatario = destinatario.nome


    @acao.setter
    def conta(self, acao: str) -> None:
        self.__acao = acao


    @valor.setter
    def valor(self, valor: str) -> None:
        self.__valor = valor
