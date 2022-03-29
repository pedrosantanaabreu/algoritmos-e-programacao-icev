"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa que receba o valor do salário-mínimo e o valor do
salário de um funcionário, calcule e mostre a quantidade de salários-mínimos
que esse funcionário ganha. 
"""

# Recebendo valores
salario_minimo = float(input("Digite o valor do salário mínimo | R$ "))
salario_funcionario = float(input("Digite o valor do salário do funcionário | R$ "))

# Calculando
salarios_recebidos = salario_funcionario / salario_minimo

# Exibindo resultado
print("\nQuantidade de salários mínimos que o funcionário ganha | {:.1f}".format(salarios_recebidos))
