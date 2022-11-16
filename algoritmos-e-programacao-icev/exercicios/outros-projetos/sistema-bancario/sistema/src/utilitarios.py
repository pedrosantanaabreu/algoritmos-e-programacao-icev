'''
Classe responsável por funções que fazem tarefas repetitivas
'''


# Módulos externos
import os


class Utilitarios:
    # Formatar
    @staticmethod
    def formatar_nome(nome: str) -> str:
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
    def formatar_cpf(cpf: str) -> str:
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
    def formatar_string(string: str) -> str:
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
    def formatar_numero(numero: str) -> str:
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
    def formatar_dinheiro(valor: str) -> str:
        if valor == '':
            return valor
        else:
            try:
                return f'{float(valor):.2f}'
            except:
                return valor


    # Outros
    @staticmethod
    def limpar_terminal() -> None:
        '''
        Limpar terminal de acordo com o sistema operacional
        '''
        
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        except:
            pass


    @staticmethod
    def imprimir_cpf_com_pontuacao(cpf: str) -> str:
        if cpf == '':
            return cpf
        else:
            try:
                resultado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
                return resultado
            except:
                return cpf
