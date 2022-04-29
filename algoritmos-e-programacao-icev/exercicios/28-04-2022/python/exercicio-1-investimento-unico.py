"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba o salário de um funcionário
chamado Carlos. Sabe-se que outro funcionário, João, tem
salário equivalente a um terço do salário de Carlos. Carlos
aplicará seu salário integralmente na caderneta de poupança,
que rende 2% ao mês, e João aplicará seu salário
integralmente no fundo de renda fixa, que rende 5% ao mês. O
programa deverá calcular e mostrar a quantidade de meses
necessários para que o valor pertencente a João iguale ou
ultrapasse o valor pertencente a Carlos.
"""

salario_carlos = float(input("[ ? ] Digite o salário de Carlos | R$ "))
salario_joao = salario_carlos / 3

montante_carlos = salario_carlos
montante_joao = salario_joao

meses = 0

while montante_joao < montante_carlos:
    montante_carlos += montante_carlos * (2 / 100)
    montante_joao += montante_joao * (5 / 100)

    meses += 1
    
print(f"\n[ / ] João levará {meses} para ultrapassar Carlos")
