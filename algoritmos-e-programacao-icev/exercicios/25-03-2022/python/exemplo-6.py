"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que 
receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu 
salário final.
"""

# Recebendo valores
salario_fixo = float(input('Digite o valor do salário | R$ '))
valor_vendas = float(input('Digite o valor das vendas | R$ '))

# Calculando
valor_comissoes = valor_vendas * 0.04
salario_final = salario_fixo + valor_comissoes

# Exibindo resultado
print('''\nSalário fixo | R$ {:.2f}
Valor comissões | R$ {:.2f}

Valor salário final | R$ {:.2f}'''.format(salario_fixo, valor_comissoes, salario_final))
