"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Sabe-se que, para iluminar de maneira correta os cômodos de
uma casa, para cada m2, deve-se usar 18 W de potência. Faça
um programa que receba as duas dimensões de um cômodo
(em metros), calcule e mostre a sua área (em m2) e a
potência de iluminação que deverá ser utilizada.
"""

# Recebendo valores
lado_1 = int(input('Digite o valor do primeiro lado | m2 '))
lado_2 = int(input('Digite o valor do segundo lado | m2 '))

# Calculando
area = lado_1 * lado_2
potencia = 18 * area

# Exibindo resultado
print('''\nÁrea | {} m2
Potência necessária | {} W
'''.format(area, potencia))
