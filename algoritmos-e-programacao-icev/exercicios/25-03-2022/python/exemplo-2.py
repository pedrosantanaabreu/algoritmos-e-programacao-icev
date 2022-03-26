"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba três números, calcule e mostre a multiplicação desses números.
"""

# Recebendo valores
numero_1 = float(input('Digite o 1º número | '))
numero_2 = float(input('Digite o 2º número | '))
numero_3 = float(input('Digite o 3º número | '))

# Calculando
resultado = numero_1 * numero_2 * numero_3

# Exibindo resultado
print('\n{:.2f} x {:.2f} x {:.2f} = {:.2f}'.format(numero_1, numero_2, numero_3, resultado))
