"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário
mínimo e a quantidade de quilowatts consumida por uma residência. Calcule e mostre:

a) o valor de cada quilowatt;

b) o valor a ser pago por essa residência;

c) o valor a ser pago com desconto de 15%.
"""

# Recebendo valores
salario_minimo = float(input('Digite o valor do salário mínimo | R$ '))
quilowatts_consumidas = float(input('Digite a quantidade de quilowatts consumidas | '))

# Calculando valores
valor_quilowatt = salario_minimo / 5
valor_residencia = valor_quilowatt * quilowatts_consumidas
valor_residencia_desconto = valor_residencia * 0.85

# Exibindo resultado
print('''
Valor de cada quilowatt | R$ {:.2f}
Valor a ser pago pela residência | R$ {:.2f}
Valor com 15% de desconto | R$ {:.2f}
'''.format(valor_quilowatt, valor_residencia, valor_residencia_desconto))
