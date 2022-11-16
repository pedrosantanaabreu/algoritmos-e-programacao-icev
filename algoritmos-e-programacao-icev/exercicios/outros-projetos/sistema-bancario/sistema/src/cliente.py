'''
Classe resposável pela criação do cliente
'''


class Cliente:
    def __init__(self, nome: str = '', cpf: str = '') -> None:
        self.__nome = nome
        self.__cpf = cpf


    # Seção getters
    @property
    def nome(self) -> str:
        return self.__nome


    @property
    def cpf(self) -> str:
        return self.__cpf


    # Seção setters
    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome


    @cpf.setter
    def cpf(self, cpf: str) -> None:
        self.__cpf = cpf
