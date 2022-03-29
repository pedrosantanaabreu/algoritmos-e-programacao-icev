"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa que receba a medida de dois ângulos de um
triângulo, calcule e mostre a medida do terceiro ângulo. sabe-se que a soma
dos ângulos de um triângulo é 180 graus
"""

# Recebendo valores
angulo_1 = float(input("Digite o 1º ângulo | "))
angulo_2 = float(input("Digite o 2º ângulo | "))

# Calculando
angulo_resultante = 180 - (angulo_1 + angulo_2)

# Exibindo resultado
print("\nO ângulo resultante será | {:.1f}°".format(angulo_resultante))
