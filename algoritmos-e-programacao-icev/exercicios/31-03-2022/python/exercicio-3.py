"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa que receba o valor do salário mínimo, o
número de horas trabalhadas, o número de dependentes do funcionário
e a quantidade de horas extras trabalhadas. Calcule e mostre o salário
a receber do funcionário de acordo com as regras a seguir:

a) O valor da hora trabalhada é igual a 1/5 do salário mínimo.

b) O salário do mês é igual ao número de horas trabalhadas multiplicado
pelo valor da hora trabalhada.

c) Para cada dependente, acrescentar R$ 32,00.

d) Para cada hora extra trabalhada, calcular o valor da hora trabalhada
acrescida de 50%.

e) O salário bruto é igual ao salário do mês
mais o valor dos dependentes mais o
valor das horas extras.

f) Calcular o valor do imposto de renda
retido na fonte de acordo com a tabela
ao lado.

g) O salário líquido é igual ao salário bruto
menos IRRF.

h) A gratificação é de acordo com a tabela
ao lado.
"""

# Recebendo valores
salario = float(input("Informe o valor do salário mínimo | R$ "))
horas = int(input("Informe a quantidade de horas trabalhadas (h) | "))
dependentes = int(input("Informe a quantidade de dependentes | "))
horas_extras = int(input("Informe a quantidade de horas extras trabalhadas (h) | "))

# Calculando
valor_hora = salario / 5
valor_hora_extra = valor_hora * 1.5
salario_receber = horas * valor_hora
salario_receber += dependentes * 32
salario_receber += horas_extras * valor_hora_extra

# Exibindo resultado
print("\nValor do salário bruto | R$ {:.2f}".format(salario_receber))

if salario_receber < 200:
    valor_imposto = 0
else:
    if salario_receber <= 500:
        valor_imposto = salario_receber * 10 / 100 
    else:
        valor_imposto = salario_receber * 20 / 100

print("\nValor do imposto | R$ {:.2f}".format(valor_imposto))
salario_receber -= valor_imposto

if salario_receber <= 350:
    valor_bonus = 100
else:
    valor_bonus = 50

print("\nValor do bônus | R$ {:.2f}".format(valor_bonus))
salario_receber += valor_bonus
print("\nValor do salário a receber | R$ {:.2f}".format(salario_receber))
