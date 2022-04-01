"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Considerando que o governo determinou um aumento anual do
salário mínimo, elabore um algoritmo que receba o valor do
salário atual e o percentual de reajuste, para depois calcular e
mostrar o valor do novo salário.
"""

# Recebendo valores
salario_atual = float(input("Informe o salário mínimo atual | R$ "))
percentual = float(input("Informe o percentual de reajuste | % "))

# Calculando
novo_salario = salario_atual * (1.0 + (percentual / 100))

# Exibindo resultado
print("\nO valor do novo salário é | R$ {:.2f}".format(novo_salario))
