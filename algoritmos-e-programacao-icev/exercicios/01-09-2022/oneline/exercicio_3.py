"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa com a seguinte especificação:
Crie uma função que receba uma string e imprima o cabeçalho com o
seguinte layout:
Utilize os caracteres +, | e – para desenhar o quadrado.
Crie uma função para desenhar a linha
Crie uma função para centralizar o texto na linha
Teste o programa com a mensagem Menu principal
"""
def imprimir_cabecalho(texto_cabecalho): print(f'+{"-" * (len(texto_cabecalho) + 8)}+\n|{" " * 4}{texto_cabecalho}{" " * 4}|\n+{"-" * (len(texto_cabecalho) + 8)}+')
