"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa que receba o custo de um espetáculo teatral e o
preço do convite desse espetáculo. Esse programa deverá calcular e mostrar
a quantidade de convites que devem ser vendidos para que, pelo menos, o
custo do espetáculo seja alcançado. 
"""

# Imports
import math

# Recebendo valores
custo_teatral = float(input('Digite o custo do espetáculo teatral | R$ '))
valor_convites = float(input('Digite o preço do convite | R$ '))

# Calculando
convites_cobrir_custo_teatral = custo_teatral / valor_convites

# Exibindo resultado
print('\nConvites necessários para cobrir custo teatral | {}'.format(math.ceil(convites_cobrir_custo_teatral)))
