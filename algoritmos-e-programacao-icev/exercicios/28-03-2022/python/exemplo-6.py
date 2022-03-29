"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa que receba o número de lados de um polígono
convexo, calcule e mostre o número de diagonais desse polígono. sabe-se
que ND = N * (N − 3) / 2, em que N é o número de lados do polígono.
"""

# Recebendo valores
lados_poligono = float(input("Digite o número de lados do poligono | "))

# Calculando
numero_diagonais = lados_poligono * (lados_poligono - 3) / 2

# Exibindo resultado
print("\nO número de diagonais do poligono é | {}".format(numero_diagonais))
