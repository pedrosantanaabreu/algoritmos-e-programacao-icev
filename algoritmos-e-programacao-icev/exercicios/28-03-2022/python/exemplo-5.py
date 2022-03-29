"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa que receba uma temperatura em Celsius, calcule
e mostre essa temperatura em Fahrenheit. Sabe-se que F = 180 * (c + 32) /
100.
"""

# Recebendo valores
temperatura_celsius = float(input("Digite a temperatura em celsius | "))

# Calculando
temperatura_fahrenheit = 180 * temperatura_celsius / 100 + 32

# Exibindo resultado
print("\nA temperatura em Fahrenheit será | {:.1f} °F".format(temperatura_fahrenheit))
