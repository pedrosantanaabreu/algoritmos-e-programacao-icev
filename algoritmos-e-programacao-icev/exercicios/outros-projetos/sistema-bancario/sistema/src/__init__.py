'''
Importando todos os arquivos para o app.py
'''


__modulos = [
    'cliente',
    'interfaces',
    'utilitarios',
    'validadores',
    'dados',
    'conta',
    'main',
    'movimentacao',
    'setup'
]


if __name__ != '__main__':
    for modulo in __modulos:
        try:
            exec(f'from .{modulo} import {modulo.title()}')
        except:
            pass
