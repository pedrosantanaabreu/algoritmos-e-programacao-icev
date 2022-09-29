"""
01) Faça um programa que imprima o conteúdo de um arquivo. O nome do arquivo deve
ser passado na linha de comando na execução do programa:
Ex: python imprimir_arquivo arquivo.txt
"""
def imprimir_arquivo(): [print(linha.removesuffix('\n')) for linha in open(input('[ - ] Insira o comando: python imprimir_arquivo exemplo.txt\n[ > ] ').strip().lower().replace('python imprimir_arquivo ', ''), 'r').readlines()]
