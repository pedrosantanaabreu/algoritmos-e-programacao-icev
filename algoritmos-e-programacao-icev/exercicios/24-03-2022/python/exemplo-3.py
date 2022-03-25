"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba uma hora (um valor para hora
e outro para minutos), calcule e mostre:

a) a hora digitada convertida em minutos;

b) o total dos minutos, ou seja, os minutos digitados mais a
conversão anterior;

c) o total dos minutos convertidos em segundos.
"""

# Recebendo dados
horas = int(input('Digite a quantidade de horas | '))
minutos =  int(input('Digite a quantidade de minutos | '))

# Calculando
hora_convertida_minutos = horas * 60
total_minutos = minutos + hora_convertida_minutos
minutos_convertido_segundos = total_minutos * 60

# Exibindo resultado
print('''\nHora digitada convertida em minutos | {}m
Total de minutos | {}m
Total de segundos | {}s
'''.format(hora_convertida_minutos, total_minutos, minutos_convertido_segundos))
