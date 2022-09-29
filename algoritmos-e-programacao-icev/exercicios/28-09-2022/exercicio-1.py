"""
01) Faça um programa que imprima o conteúdo de um arquivo. O nome do arquivo deve
ser passado na linha de comando na execução do programa:
Ex: python imprimir_arquivo arquivo.txt
"""
def imprimir_arquivo(): imprimir_arquivo = {'count' : 1, 'import' : lambda: exec('import os') or exec("os.system('cls||clear')"), 'inicial' : lambda: imprimir_arquivo['import']() or [[imprimir_arquivo['import']() or print(f'[ - ] Resultado\n{linha}', end='') or imprimir_arquivo.pop('count')] if imprimir_arquivo.get('count', 'segundo') != 'segundo' else print(linha.removesuffix('\n')) for linha in open(input('[ - ] Insira o comando: python imprimir_arquivo exemplo.txt\n[ > ] ').strip().lower().replace('python imprimir_arquivo ', ''), 'r' ).readlines()], 'enter' : lambda: input('[ - ] Digite "Enter" para continuar...')}; imprimir_arquivo['inicial']() and imprimir_arquivo['enter']()
