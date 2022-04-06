"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um algoritmo que receba as informações
necessárias, calcule e exiba o valor do salário líquido de um
trabalhador, detalhando o valor calculado para o INSS e
imposto de renda.
"""

# Recebendo valores
salario_bruto = float(input("Informe o valor do salário bruto | R$ "))
numero_dependentes = int(input("Informe o número de dependentes | "))
pensao_alimenticia = float(input("Informe o valor da pensão alimenticia | R$ "))
programa_alimentacao_trabalhador = float(input("Informe o valor do PAT (Programa de Alimentação do Trabalhador) | R$ "))
plano_saude = float(input("Informe o valor do plano de saúde | R$ "))
outros_descontos = float(input("Informe o valor de outros descontos | R$ "))

# Calculando INSS
if salario_bruto <= 1212:
    inss = salario_bruto * (7.5 / 100)
    inss_texto = "7.5 %"

elif salario_bruto <= 2427.35:
    inss = salario_bruto * (9 / 100)
    inss_texto = "9 %"

elif (salario_bruto <= 3641.03):
    inss = salario_bruto * (12 / 100)
    inss_texto = "12 %"

elif (salario_bruto <= 7087.22):
    inss = salario_bruto * (14 / 100)
    inss_texto = "14 %"

else:
    inss = 828.39
    inss_texto = "Teto"

# Calculando IRRF
base_de_calculo = salario_bruto - inss - pensao_alimenticia - numero_dependentes * 189.59
if base_de_calculo <= 1903.98:
    irrf  = base_de_calculo * (0 / 100) - 0
    irrf_texto = "0 %"

elif base_de_calculo <= 2826.65:
    irrf  = base_de_calculo * (7.5 / 100) - 142.80
    irrf_texto = "7.5 %"

elif base_de_calculo <= 3751.05:
    irrf  = base_de_calculo * (15 / 100) - 354.80
    irrf_texto = "15 %"

elif base_de_calculo <= 4664.68:
    irrf  = base_de_calculo * (22.5 / 100) - 636.13
    irrf_texto = "22.5 %"

else:
    irrf  = base_de_calculo * (27.5 / 100) - 869.36
    irrf_texto = "27.5 %"

# Calculando outros descontos
outros_descontos_total = pensao_alimenticia + programa_alimentacao_trabalhador + plano_saude + outros_descontos 
soma_descontos = inss + irrf + outros_descontos_total
salario_liquido = salario_bruto - soma_descontos
descontos_porcentagem = (salario_bruto - salario_liquido) / salario_bruto * 100

# Exibindo resultado
print("""
SALÁRIO LÍQUIDO | R$ {:.2f}
DESCONTOS | {:.2f} %

PROVENTOS,
Salário Bruto | R$ {:.2f}

DESCONTOS
INSS | {} | R$ {:.2f}
IRRF | {} | R$ {:.2f}
Outros descontos | R$ {:.2f}

TOTAL
PROVENTOS | R$ {:.2f}
DESCONTOS | R$ {:.2f} 

RESULTADO | R$ {:.2f}
""".format(salario_liquido,
descontos_porcentagem,
salario_bruto,
inss_texto,
inss,
irrf_texto,
irrf,
outros_descontos_total,
salario_bruto,
soma_descontos,
salario_liquido))
