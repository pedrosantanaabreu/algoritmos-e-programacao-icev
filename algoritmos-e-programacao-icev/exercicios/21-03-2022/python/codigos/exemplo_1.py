"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
- Exemplo 1 da aula de Algoritmos e Programação dia 21/03/2022
Faça um programa que receba o -salário base- de um funcionário, calcule e mostre o -salário a receber- , sabendo-se
 que o funcionário tem -gratificação de 5%- sobre o salário base e paga -imposto de 7%- também sobre o salário base.
"""

# Recebendo o salário base
salario_base = float(input('Digite o salário do funcionário:\nR$ '))

# Obtendo valores do bônus e imposto
bonus = salario_base * 0.05
imposto = salario_base * 0.07

# Calculando salário a receber
salario_receber = salario_base + bonus - imposto

# Exibindo resultado
print('''
Salário base | R$ {:.2f}
Bônus | R$ + {:.2f}
Imposto | R$ - {:.2f}\n
Salário a receber | R$ {:.2f}
'''.format(salario_base, bonus, imposto, salario_receber))
