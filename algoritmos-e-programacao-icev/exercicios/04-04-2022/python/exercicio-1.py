"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um algoritmo considerando três valores X, Y e Z e verifique
se eles podem ser os comprimentos dos lados de um triângulo. Se
forem, verifique se é um triângulo equilátero, isósceles ou escaleno. Se
eles não formarem um triângulo, escreva uma mensagem indicando essa
situação. Considere que:
a) o comprimento de cada lado de um triângulo é menor que a soma dos
outros dois lados;
b) considera-se equilátero o triângulo que possui três lados iguais;
Exercícios
c) denomina-se isósceles o triângulo que tem o comprimento de dois lados
iguais;
d) recebe o nome de escaleno o triângulo que tem os três lados diferentes.
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
