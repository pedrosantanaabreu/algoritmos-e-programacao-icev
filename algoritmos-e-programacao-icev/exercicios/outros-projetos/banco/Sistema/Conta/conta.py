from Utilitarios.validadores import Validadores


class Conta:
    def __init__(self, AGENCIA: str, CONTA: str, CPF: str):
        self.__AGENCIA = AGENCIA
        self.__CONTA = CONTA
        self.__CPF = CPF
    

    @property
    def AGENCIA(self):
        return self.__AGENCIA


    @property
    def CONTA(self):
        return self.__CONTA


    @property
    def CPF(self):
        return self.__CPF


    @AGENCIA.setter
    def AGENCIA(self, AGENCIA: str):
        if Validadores.validar_agencia(AGENCIA):
            self.__AGENCIA = AGENCIA
        else:
            print(f'[ ! ] A agência "{AGENCIA}" é inválida.')


    @CONTA.setter
    def CONTA(self, CONTA: str):
        if Validadores.validar_conta(CONTA):
            self.__CONTA = CONTA
        else:
            print(f'[ ! ] A conta "{CONTA}" é inválida.')


    @CPF.setter
    def CPF(self, CPF: str):
        if Validadores.validar_cpf(CPF):
            self.__CPF = self.formatar_cpf(CPF)
        else:
            print(f'[ ! ] O CPF "{CPF}" é inválido.')

