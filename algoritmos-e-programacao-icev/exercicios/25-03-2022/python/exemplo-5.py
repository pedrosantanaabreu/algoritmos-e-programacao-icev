"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba o preço de um produto, calcule e 
mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
"""

# Recebendo valores
preco_produto = float(input('Digite o valor do produto | R$ '))

# Calculando
desconto = preco_produto * 0.10
preco_desconto = preco_produto - desconto

# Exibindo resultado
print('''\nValor sem desconto | R$ {:.2f}
Desconto | - R$ {:.2f}
Valor com desconto | R$ {:.2f}'''.format(preco_produto, desconto, preco_desconto))
