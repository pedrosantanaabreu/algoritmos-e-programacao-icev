"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Escreva um programa para ler 3 valores inteiros (considere que não serão lidos valores iguais) e 
escrevê-los em ordem crescente e decrescente.
"""

# Recebendo valores
valor_1 = int(input("Digite o 1º valor | "))
valor_2 = int(input("Digite o 2º valor | "))
valor_3 = int(input("Digite o 3º valor | "))

# Encontrando o maior valor
maior = valor_1
if valor_2 > valor_3 and valor_2 > valor_1:
    maior = valor_2

if valor_3 > valor_2 and valor_3 > valor_1:
    maior = valor_3

# Encontrando valor central
meio = valor_1
if (valor_1 < valor_2 and valor_2 < valor_3) or (valor_1 > valor_2 and valor_2 > valor_3):
    meio = valor_2

if (valor_1 < valor_3 and valor_3 < valor_2) or (valor_1 > valor_3 and valor_3 > valor_2):
    meio = valor_3

# Encontrando o menor valor
menor = valor_1
if valor_2 < valor_3 and valor_2 < valor_1:
    menor = valor_2

if valor_3 < valor_2 and valor_3 < valor_1:
    menor = valor_3

# Exibindo resultado
print(f"""{valor_1} {valor_2} {valor_3} | Números digitados

{menor} {meio} {maior} | Crescente
{maior} {meio} {menor} | Decrescente
""")
