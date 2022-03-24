"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
- Exemplo 2 da aula de Algoritmos e Programação dia 21/03/2022
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos
impostos aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual
de lucro do distribuidor e o percentual de impostos, calcure e mostre:

a) o valor correspondente ao lucro do distribuidor,

b) o valor correspondente aos impostos;

c) o preço final do veículo.
"""

# Recebendo valores
preco_fabrica = float(input('Digite o preço de fábrica do veículo | R$ '))
percentual_distribuidor = float(input('Digite o percentual de lucro do distribuidor | % '))
percentual_impostos = float(input('Digite o percentual de impostos | % '))

# Calculando valor distribuidor e impostos
valor_distribuidor = preco_fabrica * percentual_distribuidor / 100
valor_impostos = preco_fabrica * percentual_impostos / 100

# Calculando preço final
preco_final = preco_fabrica + valor_distribuidor + valor_impostos

# Exibindo resultados
print('''
Lucro do distribuidor | R$ {:.2f}
Valor correspondente aos impostos | R$ {:.2f}
Preço final | R$ {:.2f}
'''.format(valor_distribuidor, valor_impostos, preco_final))
