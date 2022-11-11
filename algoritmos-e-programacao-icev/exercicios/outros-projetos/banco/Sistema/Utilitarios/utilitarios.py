import os
import importlib

class Utilitarios:
    def __init__(self):
        self.__importar_modulos()


    def __importar_modulo(self, nome, caminho):
        localizacao = importlib.util.spec_from_file_location(nome, caminho)
        modulo = importlib.util.module_from_spec(localizacao)
        localizacao.loader.exec_module(modulo)

        return modulo


    def __importar_modulos(self):
        self.__utilitarios = self.__importar_modulo('utilitarios', 'Sistema\\Utilitarios\\utilitarios.py')
        self.__interfaces = self.__importar_modulo('interfaces', 'Sistema\\Interfaces\\interfaces.py')


    @staticmethod
    def limpar_terminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    

    @staticmethod
    def enter_para_continuar():
        input('| -> ')


    @classmethod
    def mensagem_de_erro(classe, texto):
        c = classe()
        c.__utilitarios.Utilitarios.limpar_terminal()
        c.__interfaces.Interfaces.imprimir_menu_mensagem_de_erro(texto)
        c.__interfaces.Interfaces.imprimir_menu_enter_para_continuar(texto)
        c.__utilitarios.Utilitarios.enter_para_continuar()
