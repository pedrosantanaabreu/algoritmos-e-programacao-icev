

class Cliente:
    def __init__(self, NOME: str, CPF: str):
        self.__NOME = self.__formatar_nome(NOME)
        self.__CPF = self.__formatar_cpf(CPF)

        if not self.__validar_informacoes_iniciais():
            print('[ ! ] Informações inválidas')
            return False 


    def __str__(self):
        return f'Classe:\
            \n\t{self.__class__}\
            \nEndereços:\
            \n\tInt: {id(self.__class__)}\
            \n\tHex: {hex(id(self.__class__))}\
            \nInformações:\
            \n\tNome:\
            \n\t\t{self.NOME}\
            \n\tCPF:\
            \n\t\t{self.CPF}'


    def __validar_informacoes_iniciais(self):
        if Validadores.validar_cpf(self.CPF) and Validadores.validar_nome(self.NOME):
            return True
        else:
            return False


    def __formatar_nome(self, nome: str):
        resultado = ''
        for palavra in nome.split():
            resultado += ' ' + palavra.strip()
        
        return resultado.title().strip()


    def __formatar_cpf(self, cpf: str):
        resultado = ''
        for caractere in str(cpf):
            if caractere.isdigit():
                resultado += caractere
            else:
                pass

        return resultado


    @property
    def NOME(self):
        return self.__NOME


    @property
    def CPF(self):
        return self.__CPF


    @NOME.setter
    def NOME(self, NOME: str):
        if Validadores.validar_nome(NOME):
            self.__NOME = self.__formatar_nome(NOME)
        else:
            print(f'[ ! ] O nome "{NOME}" é inválido.')


    @CPF.setter
    def CPF(self, CPF: str):
        if Validadores.validar_cpf(CPF):
            self.__CPF = self.__formatar_cpf(CPF)
        else:
            print(f'[ ! ] O CPF "{CPF}" é inválido.')
