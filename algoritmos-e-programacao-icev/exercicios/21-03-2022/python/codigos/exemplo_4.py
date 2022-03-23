"""
@Pedro Santana Abreu
@Icev

PT-BR:
Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui.
Ela vai passar por vários países e precisa converter seu dinheiro em dólares, euros e libra esterlina.
Sabe-se que a cotarão do dólar é de R$ 4,25; do euro, de R$ 4,75; e da libra esterlina, de R$ 5,64.
O programa deve fazer as conversões e mostrá-las.
"""

# Cotações
euro = 4.75
dolar = 4.25
libra_esterlina = 5.64

# Recebendo valor em reais
valor_reais = float(input('Digite o valor em reais | R$ '))

# Conversões
real_euro = valor_reais / euro
real_dolar = valor_reais / dolar
real_libra_esterlina = valor_reais / libra_esterlina

# Exibindo resultados
print('''
Valor em reais | R$ {:.2f}\n
Euro | € {:.2f}
Dolar | $ {:.2f}
Libra Esterlina | £ {:.2f}
'''.format(valor_reais, real_euro, real_dolar, real_libra_esterlina))
