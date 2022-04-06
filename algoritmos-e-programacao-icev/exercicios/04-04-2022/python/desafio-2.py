"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um algoritmo que receba o peso (em quilograma)
e a altura (em metros) de uma pessoa e exiba o valor do IMC,
a avaliação do peso dessa pessoa e qual seria a faixa de peso
ideal.
"""

# Recebendo valores
altura = float(input("Informe a altura (m) | "))
peso = float(input("Informe o peso (kg) | "))

# Calculando IMC
imc = peso / (altura * altura)
if imc <= 15:
    print("\nExtremamente abaixo do peso")

elif imc <= 16:
    print("\nGravemente abaixo do peso")

elif imc <= 18.5:
    print("\nAbaixo do peso ideal")

elif imc <= 25:
    print("\nFaixa de peso ideal")

elif imc <= 30:
    print("\nSobrepeso")

elif imc <= 35:
    print("\nObesidade grau I")

elif imc <= 40:
    print("\nObesidade grau II (grave)")

else:
    print("\nObesidade grau III (mórbida)")

peso_ideal_menor = altura * altura * 18.5
peso_ideal_maior = altura * altura * 25.0

# Exibindo resultado
print("""
IMC | {:.2f}
PESO IDEAL | {:.2f} - {:.2f}""".format(imc, peso_ideal_menor, peso_ideal_maior))
