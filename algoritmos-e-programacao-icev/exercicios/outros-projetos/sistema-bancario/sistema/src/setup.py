"""
Arquivo com finalidade de certificar se o usuário tem todas as pendências necessárias
"""


# Módulos externos
import os
import subprocess
import sys


class Setup:
    # Path
    __path = {
        'bibliotecas': '..\sistema\src\\bibliotecas.txt',
        'arquivos_py': '..\sistema\src\\',
        'arquivos_csv' : '..\sistema\src\dados\\'
    }


    # Arquivos
    __bibliotecas_necessarias_setup = [
        'rich'
    ]

    __arquivos_banco_de_dados_necessarios_setup = [
        'clientes.csv',
        'contas.csv',
        'movimentacoes.csv'
    ]

    __arquivos_py_necessarios_setup = [
        '__init__.py',
        'cliente.py',
        'conta.py',
        'dados.py',
        'interfaces.py',
        'main.py',
        'movimentacao.py',
        'setup.py',
        'utilitarios.py',
        'validadores.py'
    ]


    @staticmethod
    def __obter_bibliotecas_instaladas() -> list:
        '''
        Cria um arquivo .txt com toda as bibliotecas instaladas do usuário.
        '''

        lista_bibliotecas = []
        bibliotecas_instaladas = (subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split('\r\n'))

        for biblioteca in bibliotecas_instaladas:
            if biblioteca != '':
                lista_bibliotecas.append(biblioteca.split('==')[0])
            else:
                pass
        return lista_bibliotecas


    @staticmethod
    def __instalar_biblioteca(biblioteca: str) -> None:
        os.system(f'pip install {biblioteca}')


    @classmethod
    def __escrever_txt_com_bibliotecas_do_usuario(cls, bibliotecas) -> None:
        with open(cls.__path['bibliotecas'] , 'w+') as arquivo_escrita:
            for biblioteca in bibliotecas:
                arquivo_escrita.write(biblioteca)
                arquivo_escrita.write('\n')


    @classmethod
    def iniciar_instalacao(cls) -> None:
        cls.__limpar_terminal()

        try:
            with open('..\sistema\src\\bibliotecas.txt', 'r') as arquivo_leitura:
                for biblioteca in cls.__bibliotecas_necessarias_setup:
                    cls.__limpar_terminal()
                    print('Instalando bibliotecas...')
                    if biblioteca not in arquivo_leitura.read():
                        bibliotecas_instaladas = cls.__obter_bibliotecas_instaladas()
                        cls.__escrever_txt_com_bibliotecas_do_usuario(bibliotecas_instaladas)
                        cls.__instalar_biblioteca(biblioteca)
                        cls.__limpar_terminal()
        except:
            print('Instalando bibliotecas...')
            bibliotecas_instaladas = cls.__obter_bibliotecas_instaladas()
            cls.__escrever_txt_com_bibliotecas_do_usuario(bibliotecas_instaladas)

            for biblioteca in cls.__bibliotecas_necessarias_setup:
                if biblioteca not in bibliotecas_instaladas:
                    cls.__instalar_biblioteca(biblioteca)
                else:
                    pass
        finally:
            cls.__verificar_arquivos_necessarios_py()
            cls.__limpar_terminal()
            cls.__verificar_arquivos_necessarios_banco_de_dados()
            cls.__limpar_terminal()
            cls.__iniciando_aplicacao()
            cls.__limpar_terminal()


    @classmethod
    def __iniciando_aplicacao(cls) -> None:
        # Módulos externos
        from rich.progress import track
        from time import sleep


        for _ in track(range(10), 'Iniciando aplicação...'):
            sleep(0.03)


    # Verificar
    @classmethod
    def __verificar_arquivos_necessarios_py(cls) -> None:
        # Módulos externos
        from rich.tree import Tree
        from rich import print as rprint
        from time import sleep
        

        erros = 0
        
        arvore = Tree('[green]Verificando todos os arquivos.py necessários...')
        segmento_src = arvore.add('src')


        for arquivo in cls.__arquivos_py_necessarios_setup:
            segmento = segmento_src.add(f'Verificando arquivo \'{arquivo}\'')
            
            cls.__limpar_terminal()
            rprint(arvore)
            sleep(0.05)


            if cls.__verificar_arquivo_py(arquivo):
                segmento.add(f'[green]Ok[/]')
            else:
                segmento.add(f'[red]Erro[/]')
                erros += 1

            cls.__limpar_terminal()
            rprint(arvore)
            sleep(0.05)

        if erros > 0:
            segmento = segmento_src.add(f'[red] Erros encontrados, verifique se todos os arquivos.py estão no src.')
            cls.__limpar_terminal()
            rprint(arvore)
            
            input()
            cls.__limpar_terminal()
            exit()
        else:
            pass


    @classmethod
    def __verificar_arquivos_necessarios_banco_de_dados(cls) -> None:
        # Módulos externos
        from rich.tree import Tree
        from rich import print as rprint
        from time import sleep


        erros = 0
        
        arvore = Tree('[green]Verificando todos os arquivos.csv necessários...')
        segmento_src = arvore.add('dados')

        for arquivo in cls.__arquivos_banco_de_dados_necessarios_setup:
            segmento = segmento_src.add(f'Verificando arquivo \'{arquivo}\'')
    
            cls.__limpar_terminal()
            rprint(arvore)
            sleep(0.05)

            if cls.__verificar_arquivo_banco_de_dados(arquivo):
                segmento.add(f'[green]Ok[/]')
            else:
                segmento.add(f'[red]Erro[/]')
                erros += 1

            cls.__limpar_terminal()
            rprint(arvore)
            sleep(0.05)

        if erros > 0:
            segmento = segmento_src.add(f'[red] Erros encontrados, verifique se todos os arquivos.csv estão no dados.')
            cls.__limpar_terminal()
            rprint(arvore)
            
            input()
            cls.__limpar_terminal()
            exit()
        else:
            pass


    @classmethod
    def __verificar_arquivo_banco_de_dados(cls, arquivo: str) -> bool:
        '''
        Tenta abrir o arquivo seleionado, caso não consiga
        sgnifica que o mesmo não existe deve ser instalado
        '''
        
        
        try:
            open(f'{cls.__path["arquivos_csv"]}{arquivo}', 'r')
            return True
        except:
            return False


    @classmethod
    def __verificar_arquivo_py(cls, arquivo: str) -> bool:
        '''
        Tenta abrir o arquivo seleionado, caso não consiga
        sgnifica que o mesmo não existe deve ser instalado
        '''
        
        
        try:
            open(f'{cls.__path["arquivos_py"]}{arquivo}', 'r')
            return True
        except:
            return False


    # Outros
    @staticmethod
    def __limpar_terminal() -> None:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
