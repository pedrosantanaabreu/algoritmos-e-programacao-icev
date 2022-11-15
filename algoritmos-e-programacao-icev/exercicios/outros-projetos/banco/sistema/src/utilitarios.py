import os


class Utilitarios:
    @staticmethod
    def limpar_terminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    

    @staticmethod
    def formatar_nome(nome: str):
        if nome == '':
            return nome
        else:
            resultado = ''
            try:
                for palavra in nome.split():
                    resultado += ' ' + palavra.strip()
                return resultado.title().strip()
            except:
                return nome


    @staticmethod
    def formatar_cpf(cpf : str):
        if cpf == '':
            return cpf
        else:
            resultado = ''
            try:
                for caractere in str(cpf):
                    if caractere.isdigit():
                        resultado += caractere
                    else:
                        pass
                return resultado
            except:
                return cpf


    @staticmethod
    def formatar_string(string : str):
        if string == '':
            return string
        else:
            resultado = ''
            try:
                for palavra in string.split():
                    resultado += '' + palavra.strip()
                return resultado
            except:
                return string


    @staticmethod
    def formatar_numero(numero : str):
        if numero == '':
            return numero
        else:
            resultado = ''
            try:
                for caractere in numero.split():
                    resultado += '' + caractere.strip()
                return resultado.strip()
            except:
                return numero


    @staticmethod
    def imprimir_cpf_com_pontuacao(cpf : str):
        if cpf == '':
            return cpf
        else:
            try:
                resultado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
                return resultado
            except:
                return cpf


    def formatar_dinheiro(valor : str):
        if valor == '':
            return valor
        else:
            return f'{float(valor):.2f}'
