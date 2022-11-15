class Cliente:
    def __init__(self, nome : str = '', cpf : str = ''):
        self.__nome = nome
        self.__cpf = cpf


    @property
    def nome(self):
        return self.__nome


    @property
    def cpf(self):
        return self.__cpf


    @nome.setter
    def nome(self, nome : str):
        self.__nome = nome


    @cpf.setter
    def cpf(self, cpf : str):
        self.__cpf = cpf
