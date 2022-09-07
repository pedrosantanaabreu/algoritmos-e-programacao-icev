"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Utilizando a função do exercício anterior, desenvolva uma função que receba um
número variável de entradas e informe para cada entrada se é par ou ímpar.
"""
def numeros_pares_ou_impares(*args): [print(f'[ - ] O número {numero} é par') if numero % 2 == 0 else print(f'[ - ] O número {numero} é ímpar') for numero in args]
