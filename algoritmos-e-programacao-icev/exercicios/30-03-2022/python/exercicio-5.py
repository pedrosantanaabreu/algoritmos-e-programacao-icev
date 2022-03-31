"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Tendo como dados de entrada a altura e o sexo de uma pessoa (M-masculino e F-feminino),
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
para homens: (72.7*h)-58
para mulheres: (62.1*h)-44.7 
Obs h = Altura. 
"""

# Recebendo valores
altura = int(input("Digite a altura em cm | "))
sexo = input("Digite (M) para masculino e (F) para feminino | ").strip().upper()

# Calculando
peso_ideal = 72.7 * altura / 100 - 58
if sexo == "F":
    peso_ideal = 62.1 * altura / 100 - 44.7 

# Exibindo resultado
print("\nPeso ideal | {} Kg".format(peso_ideal))
