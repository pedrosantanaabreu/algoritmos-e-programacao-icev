"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Pedro comprou um saco de ração com peso em quilos. Ele
possui dois gatos, para os quais fornece a quantidade de
ração em gramas. A quantidade diária de ração fornecida
para cada gato é sempre a mesma. Faça um programa que
receba o peso do saco de ração e a quantidade de ração
fornecida para cada gato, calcule e mostre quanto restará de
ração no saco após cinco dias.
"""

# Recebendo valores
peso_saco = float(input('Digite o peso do saco de ração | KG '))
quantidade_racao_gato = float(input('Digite a quantidade de ração fornecida para cada gato | g '))

# Calculando
resultado_racao = peso_saco * 1000 - (quantidade_racao_gato * 5) * 2

# Exibindo resultado
print('\nRestará no final de 5 dias {:.2f} g de ração'.format(resultado_racao))
