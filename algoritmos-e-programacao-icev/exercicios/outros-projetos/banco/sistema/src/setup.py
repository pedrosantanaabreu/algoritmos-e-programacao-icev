import os
import subprocess
import sys



class Setup:
    @staticmethod
    def __obter_bibliotecas_instalads():
        bibliotecas_instaladas = reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8')
        bibliotecas_instaladas = bibliotecas_instaladas.split('\r\n')
        bibliotecas_instaladas = [pkg.split('==')[0] for pkg in bibliotecas_instaladas if pkg != '']
        return bibliotecas_instaladas
    

    @staticmethod
    def __instalar_bibliotecas(biblioteca : str):
        os.system(f'pip install {biblioteca}')
    

    @classmethod
    def iniciar_instalacao(cls):
        bibliotecas_instaladas = cls.__obter_bibliotecas_instalads()
        bibliotecas = ['rich']

        for biblioteca in bibliotecas:
            if biblioteca not in bibliotecas_instaladas:
                cls.__instalar_bibliotecas(biblioteca)
            else:
                pass
