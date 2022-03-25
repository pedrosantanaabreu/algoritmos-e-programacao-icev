"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba o número de horas trabalhadas, o valor
do salário mínimo e o número de horas extras trabalhadas, calcule e
mostre o salário a receber, de acordo com as regras a seguir:

a) a hora trabalhada vale 1/8 do salário mínimo;

b) a hora extra vale 1/4 do salário mínimo;

c) o salário bruto equivale ao número de horas trabalhadas multiplicado
pelo valor da hora trabalhada;

d) a quantia a receber pelas horas extras equivale ao número de horas
extras trabalhadas multiplicado pelo valor da hora extra;

e) o salário a receber equivale ao salário bruto mais a quantia a receber
pelas horas extras.
"""

# Recebendo valores
horas_trabalhadas = int(input('Digite o número de horas trabalhadas | '))
salario_minimo = float(input('Digite o valor so salário mínimo | R$ '))
horas_extras = int(input('Digite as horas extras | '))

# Cálculos
hora_trabalhada_valor = salario_minimo / 8
hora_extra_valor = salario_minimo / 4
hora_extra_total = hora_extra_valor * horas_extras
hora_trabalhada_total = hora_trabalhada_valor * horas_trabalhadas
salario_receber = hora_extra_total + hora_trabalhada_total

# Exibindo resultado
print("""\nValor de cada hora trabalhada | R$ {:.2f}
Valor de cada hora extra | R$ {:.2f}

Valor referente as horas trabalhadas | R$ {:.2f}
Valor referente as horas extras | R$ {:.2f}

Valor do salário a receber | R$ {:.2f}
""".format(hora_trabalhada_valor, hora_extra_valor, hora_trabalhada_total, hora_extra_total, salario_receber))
