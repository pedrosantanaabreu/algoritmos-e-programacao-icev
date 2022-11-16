'''
Importando todos os arquivos para o app.py
'''


if __name__ != '__main__':
    try:
        from .cliente import Cliente
        from .interfaces import Interfaces
        from .utilitarios import Utilitarios
        from .validadores import Validadores
        from .dados import Dados
        from .conta import Conta
        from .main import Main
        from .movimentacao import Movimentacao
        from .setup import Setup
    except:
        pass
