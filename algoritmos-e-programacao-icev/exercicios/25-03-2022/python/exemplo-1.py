"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.
"""

# Recebendo valores
numero_1 = float(input('Digite o 1º número | '))
numero_2 = float(input('Digite o 2º número | '))

# Calculando
resultado = numero_1 - numero_2

# Exibindo resultado
print('\n{:.2f} - {:.2f} = {:.2f}'.format(numero_1, numero_2, resultado))
