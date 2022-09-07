"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Utilizando a função do exercício anterior, desenvolva uma função que receba um
número variável de entradas e informe para cada entrada se é par ou ímpar.
"""
def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'


def numeros_pares_ou_impares(*args):
    lista = []
    for numero in args:
        lista.append((numero, par_ou_impar(numero)))
    return lista
