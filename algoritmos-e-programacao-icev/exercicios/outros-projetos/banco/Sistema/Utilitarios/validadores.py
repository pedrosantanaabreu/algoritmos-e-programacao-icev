class Validadores:
    @classmethod
    def validar_nome(classe, nome):
        if classe.formatar_string(nome).isalpha():
            return True
        else:
            return False


    @staticmethod
    def formatar_cpf(cpf):
        resultado = ''
        for caractere in str(cpf):
            if caractere.isdigit():
                resultado += caractere
            else:
                pass
        return resultado


    @staticmethod
    def obter_digitos_verificadores(numeros):
        resultado_soma_digitos = 0

        for index, multiplicador in enumerate(numeros):
            resultado_soma_digitos += (10 - index) * int(multiplicador)

        if resultado_soma_digitos % 11 <= 1:
            digito_final = 0
        else:
            digito_final = 11 - resultado_soma_digitos % 11

        return digito_final


    @classmethod
    def validar_cpf(classe, cpf):
        cpf = classe.formatar_cpf(cpf)

        if len(cpf) == 11:
            primeiro_digito_verificador = int(cpf[-2])
            segundo_digito_verificador = int(cpf[-1])

            calculo_primeiro_digito = classe.obter_digitos_verificadores(cpf[0:9])
            calculo_segundo_digito = classe.obter_digitos_verificadores(cpf[1:10])

            if calculo_primeiro_digito == primeiro_digito_verificador and calculo_segundo_digito == segundo_digito_verificador:
                return True
            else:
                return False
        else:
            return False


    @classmethod
    def validar_agencia(classe, agencia):
        if classe.formatar_numero(agencia).isnumeric():
            return True
        else:
            return False


    @staticmethod
    def formatar_string(string):
        resultado = ''
        for palavra in string.split():
            resultado += '' + palavra.strip()
        
        return resultado.title().strip()


    @staticmethod
    def formatar_numero(numero):
        resultado = ''
        for caractere in numero.split():
            resultado += '' + caractere.strip()
        
        return resultado.strip()
    

    @classmethod
    def validar_conta(classe, conta):
        if classe.formatar_numero(conta).isnumeric():
            return True
        else:
            return False


    @staticmethod
    def validar_opcao_menu(opcoes_menu, opcao_usuario):
        try:
            opcao_usuario = int(opcao_usuario)
            if opcao_usuario in list(range(1, opcoes_menu + 1)):
                return True
            else:
                return False
        except:
            return False
