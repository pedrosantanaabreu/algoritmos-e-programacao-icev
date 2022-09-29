"""
02) Editor de Texto Simples:
Faça um programa que leia linhas de texto até que seja informado uma linha em
branco.
Depois ler o nome do arquivo e salvar as linhas digitadas no arquivo com esse nome.
"""
def imprimir_ate_linha_em_branco(): imprimir_ate_linha_em_branco = {'lista' : [], 'escrever' : [lambda lista: [open(input('[ - ] Informe o nome do arquivo (exemplo.txt)\n[ > ] ').strip().lower(), 'w').writelines(lista)]], 'receber' : [lambda lista: [lista.append(input(f'[ - ] Informe uma linha ou uma linha em branco para fechar\n[ > ] ') + '\n') if '\n' not in lista else imprimir_ate_linha_em_branco['escrever'][0](lista) and exit() for _, __ in enumerate(iter(bool, True))]]}; imprimir_ate_linha_em_branco['receber'][0](imprimir_ate_linha_em_branco['lista']) if True else ''
