'''
Importando todos os arquivos para o app.py
'''


if __name__ != '__main__':
    __modulos_init_ = [
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
    
    
    for modulo_init in __modulos_init_:
        try:
            exec(f'from .{modulo_init} import {modulo_init.title()}')
        except:
            pass
