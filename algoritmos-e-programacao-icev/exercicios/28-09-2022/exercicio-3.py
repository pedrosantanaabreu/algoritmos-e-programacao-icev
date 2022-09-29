"""
03) Concatenar dois arquivos
Crie um programa que receba o nome de dois arquivos como parâmetros da linha de
comando e que gere um arquivo de saída com as linhas do primeiro e do segundo
arquivo.
"""
def concatenar(): open(input('[ - ] Informe o nome do arquivo final (exemplo.txt)\n[ > ] ').strip().lower(), 'w').writelines((open(input('[ - ] Informe o 1º arquivo (exemplo.txt)\n[ > ] ').strip().lower(), 'r').readlines() + ['\n'] + open(input('[ - ] Informe o 2º arquivo (exemplo.txt)\n[ > ] ').strip().lower(), 'r').readlines()))
