"""
04) Contador de palavras
Escreva um programa que conte quantas vezes cada palavra aparece em um arquivo.
O arquivo deve ser passado da linha de comando.
Deverá ser listada cada palavra do arquivo e o contador da palavra ao seu lado.
"""
def quantidade_de_palavras(): quantidade_de_palavras = {'lista_palavras' : [], 'obter' : lambda: [quantidade_de_palavras["lista_palavras"].extend(linha.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('(', '').replace(')', '').replace(':', '').strip().lower().split()) for linha in open(input('[ - ] Informe o arquivo (exemplo.txt)\n[ > ] ').strip().lower(), "r")], 'resultado' : lambda: [print(f'''[ - ] A palavra "{palavra}" apareceu {quantidade_de_palavras["lista_palavras"].count(palavra)} vez(es)''') for palavra in set(quantidade_de_palavras["lista_palavras"])], 'inicar' : lambda: quantidade_de_palavras['obter']() and  quantidade_de_palavras['resultado']() if True else ''}; quantidade_de_palavras['inicar']() if True else ''
