"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, 
considerando peso 2 para a primeira e peso 3 para a segunda.
"""

# Recebendo valores
nota_1 = float(input('Digite a 1ª nota | '))
nota_2 = float(input('Digite a 2ª nota | '))

# Calculando
media = (nota_1 + nota_2) / 2

# Exibindo resultado
print('\nResultado média | {:.1f}'.format(media))
