class Cores:
    def __init__(self):
        self.dicionario_de_cores_e_estilos = {
            'fim' : '\033[m',

            'estilo' : {
                '' : 0,
                'nehum': 0,
                'negrito': 1,
                'sublinhado': 4,
                'inverter': 7
            },

            'cor do texto' : {
                '' : 0,
                'branco': 30,
                'vermelho': 31,
                'verde': 32,
                'amarelo': 33,
                'azul': 34,
                'magenta': 35,
                'cyan': 36,
                'cinza': 37
            },

            'cor de fundo' : {
                '' : 0,
                'branco': 40,
                'vermelho': 41,
                'verde': 42,
                'amarelo': 43,
                'azul': 44,
                'magenta': 45,
                'cyan': 46,
                'cinza': 47
            }
        }

    def print_personalizado(self, cor_do_texto = '', cor_de_fundo = '',  estilo = '', texto = ''):
        print(f'\033[{self.dicionario_de_cores_e_estilos["estilo"][estilo]};{self.dicionario_de_cores_e_estilos["cor do texto"][cor_do_texto]};{self.dicionario_de_cores_e_estilos["cor de fundo"][cor_de_fundo]}m{texto}{self.dicionario_de_cores_e_estilos["fim"]}', end='')


    def print_personalizado_personalizado(self, codigo_do_texto = '', codigo_do_fundo = '',  codigo_do_estilo = '', texto = ''):
        print(f'\033[{codigo_do_estilo};{codigo_do_texto};{codigo_do_fundo}m{texto}{self.dicionario_de_cores_e_estilos["fim"]}', end='')
