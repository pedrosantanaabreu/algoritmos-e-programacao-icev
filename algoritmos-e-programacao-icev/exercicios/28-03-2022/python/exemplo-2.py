"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
Desenvolva um programa que receba o salário fixo do funcionário e o valor
de suas vendas, calcule e mostre a comissão e seu salário final.  
"""

# Recebendo valores
salario_fixo = float(input("Digite o valor do salário | R$ "))
valor_vendas = float(input("Digite o valor das vendas | R$ "))

# Calculando
comissao = valor_vendas * 0.04
salario_final = salario_fixo + comissao

# Exibindo resultado
print("""\nValor salário fixo | R$ {:.2f}
Valor das comissões | R$ {:.2f}
\nValor final do salário | R$ {:.2f}""".format(salario_fixo, comissao, salario_final))
