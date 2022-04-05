"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Escreva um programa que leia as medidas dos lados de um triângulo e escreva se ele é Equilátero, 
Isósceles ou Escaleno. Sendo que:
Triângulo Equilátero: possui os 3 lados iguais.
Triângulo Isóscele: possui 2 lados iguais.
Triângulo Escaleno: possui 3 lados diferentes
Obs.: O programa deverá informar se os valores podem ser um triângulo.
"""

# Recebendo valores
lado_1 = float(input("1º lado | "))
lado_2 = float(input("2º lado | "))
lado_3 = float(input("3º lado | "))

# Calculando
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    if lado_1 == lado_2 and lado_2 == lado_3:
        print("\nTriângulo equilátero")
    elif lado_1 != lado_2 and lado_2 != lado_3:
        print("\nTriângulo escaleno")
    else:
        print("\nTriângulo isósceles")
else:
    print("\nOs lados não formam um triângulo")
