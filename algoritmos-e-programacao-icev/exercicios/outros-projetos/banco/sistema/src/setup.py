import os
import subprocess
import sys


class Setup:
    @staticmethod
    def __obter_bibliotecas_instaladas():
        bibliotecas_instaladas = reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
        bibliotecas_instaladas = bibliotecas_instaladas.split('\r\n')
        bibliotecas_instaladas = [pkg.split('==')[0] for pkg in bibliotecas_instaladas if pkg != '']
        return bibliotecas_instaladas
    

    @staticmethod
    def __instalar_bibliotecas(biblioteca : str):
        os.system(f'pip install {biblioteca}')


    @staticmethod
    def __escrever_blbiotecas(bibliotecas):
        with open('..\sistema\src\\bibliotecas.txt', 'w+') as arquivo_escrita:
            for biblioteca in bibliotecas:
                arquivo_escrita.write(biblioteca)
                arquivo_escrita.write('\n')


    @classmethod
    def iniciar_instalacao(cls):
        bibliotecas = ['rich']
        cls.__limpar_terminal()
        

        try:
            with open('..\sistema\src\\bibliotecas.txt', 'r') as arquivo_leitura:
                for biblioteca in bibliotecas:
                    if biblioteca not in arquivo_leitura.read():
                        print('Instalando bibliotecas...')
                        bibliotecas_instaladas = cls.__obter_bibliotecas_instaladas()
                        cls.__escrever_blbiotecas(bibliotecas_instaladas)
                        for biblioteca in bibliotecas:
                            
                            if biblioteca not in bibliotecas_instaladas:
                                cls.__instalar_bibliotecas(biblioteca)
                            else:
                                pass
        except:
            print('Instalando bibliotecas...')
            bibliotecas_instaladas = cls.__obter_bibliotecas_instaladas()
            cls.__escrever_blbiotecas(bibliotecas_instaladas)

            for biblioteca in bibliotecas:
                
                if biblioteca not in bibliotecas_instaladas:
                    cls.__instalar_bibliotecas(biblioteca)
                else:
                    pass
        finally:
            cls.__verificar_arquivos_necessarios_py()
            cls.__verificar_arquivos_necessarios_banco_de_dados()
            cls.__iniciar()


    @classmethod
    def __iniciar(cls):
        from rich.console import Console
        from rich.progress import track
        from time import sleep

        cls.__limpar_terminal()
        for _ in track(range(10), 'Iniciando aplicação...'):
            sleep(0.03)


    @classmethod
    def __verificar_arquivos_necessarios_py(cls):
        from rich.console import Console
        from rich.tree import Tree
        from rich import print as rprint
        from time import sleep

        arquivos_py = [
            ('Verificando arquivo __init__.py', '__init__.py'),
            ('Verificando arquivo cliente.py', 'cliente.py'),
            ('Verificando arquivo conta.py', 'conta.py'),
            ('Verificando arquivo dados.py', 'dados.py'),
            ('Verificando arquivo interfaces.py', 'interfaces.py'),
            ('Verificando arquivo main.py', 'main.py'),
            ('Verificando arquivo movimentacao.py', 'movimentacao.py'),
            ('Verificando arquivo setup.py', 'setup.py'),
            ('Verificando arquivo utilitarios.py', 'utilitarios.py'),
            ('Verificando arquivo validadores.py', 'validadores.py')
        ]

        erro = 0
        console = Console()
        tree = Tree('[green]Verificando todos os arquivos.py necessários...')
        segmente_src = tree.add('src')

        for arquivo in arquivos_py:
            segmento = segmente_src.add(f'{arquivo[0]}')
            cls.__limpar_terminal()
            rprint(tree)
            sleep(0.05)

            if cls.__verificar_arquivos_py(arquivo[1]):
                segmento.add(f'[green]Concluído[/]')
            else:
                segmento.add(f'[red]Erro[/]')
                erro = 1
                

            cls.__limpar_terminal()
            rprint(tree)
            sleep(0.05)

        if erro == 1:
            segmento = segmente_src.add(f'[red] Erros encontrados, verifique se todos os arquivos.py estão no src.')
            cls.__limpar_terminal()
            rprint(tree)
            input()


    @classmethod
    def __verificar_arquivos_necessarios_banco_de_dados(cls):
        from rich.console import Console
        from rich.tree import Tree
        from rich import print as rprint
        from time import sleep

        arquivos_banco_de_dados = [
            ('Verificando arquivo clientes.csv', 'clientes.csv'),
            ('Verificando arquivo contas.csv', 'contas.csv'),
            ('Verificando arquivo movimentacoes.csv', 'movimentacoes.csv')
        ]

        erro = 0
        console = Console()
        tree = Tree('[green]Verificando todos os arquivos.csv necessários...')
        segmente_src = tree.add('dados')

        for arquivo in arquivos_banco_de_dados:
            segmento = segmente_src.add(f'{arquivo[0]}')
            cls.__limpar_terminal()
            rprint(tree)
            sleep(0.05)

            if cls.__verificar_arquivos_banco_de_dados(arquivo[1]):
                segmento.add(f'[green]Concluído[/]')
            else:
                segmento.add(f'[red]Erro[/]')
                erro = 1
                

            cls.__limpar_terminal()
            rprint(tree)
            sleep(0.05)

        if erro == 1:
            segmento = segmente_src.add(f'[red] Erros encontrados, verifique se todos os arquivos.csv estão no dados.')
            cls.__limpar_terminal()
            rprint(tree)
            input()


    @staticmethod
    def __verificar_arquivos_banco_de_dados(arquivo):
        try:
            open(f'..\sistema\src\dados\{arquivo}', 'r')
            return True
        except:
            return False


    @staticmethod
    def __verificar_arquivos_py(arquivo):
        try:
            open(f'..\sistema\src\{arquivo}', 'r')
            return True
        except:
            return False
    

    @staticmethod
    def __limpar_terminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
