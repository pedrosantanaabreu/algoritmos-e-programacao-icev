"""
03) Concatenar dois arquivos
Crie um programa que receba o nome de dois arquivos como parâmetros da linha de
comando e que gere um arquivo de saída com as linhas do primeiro e do segundo
arquivo.
"""
def concatenar(): concatenar = {'import' : lambda: exec('import os') or exec("os.system('cls||clear')"),'iniciar' : lambda: concatenar['import']() or open(input('[ - ] Informe o nome do arquivo final (exemplo.txt)\n[ > ] ').strip().lower(), 'w').writelines(concatenar['import']() or (open(input('[ - ] Informe o 1º arquivo (exemplo.txt)\n[ > ] ').strip().lower(), 'r').readlines() + ['\n'] + open(concatenar['import']() or input('[ - ] Informe o 2º arquivo (exemplo.txt)\n[ > ] ').strip().lower(), 'r').readlines())) or concatenar['import']() or input('[ - ] Arquivo criado com sucesso\n[ - ] Digite "Enter" para continuar...')}; concatenar['iniciar']()
