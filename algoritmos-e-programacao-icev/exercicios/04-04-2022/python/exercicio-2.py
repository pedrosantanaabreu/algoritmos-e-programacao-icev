"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um algoritmo que receb0a
a) O código de um produto comprado, supondo que a digitação do código
do produto seja sempre válida, isto é, um número inteiro entre 1 e 10.
b) O peso do produto em quilogramas.
c) O código do país de origem, supondo que a digitação do código seja
sempre válida, isto é, um número inteiro entre 1 e 3.
Exercícios
Considerando as tabelas apresentadas, calcule e mostre:
I. o peso do produto convertido em gramas;
II. o preço total do produto comprado;
III. o valor do imposto, sabendo que ele é cobrado sobre o preço total do
produto comprado e depende do país de origem;
IV. o valor total, preço total do produto mais imposto.
"""

# Recebendo valores
codigo_produto = int(input("Informe o código do produto (1 a 10) | "))
codigo_pais_origem = int(input("Informe o código do país de origem (1 a 3) | "))
peso_produto_kg = float(input("Informe o peso do produto (kg) | "))

# Convertendo kg para g, calculando valor total do produto e imposto
peso_produto_g = peso_produto_kg * 1000
if (codigo_produto >= 1 and codigo_produto <= 10) and (codigo_pais_origem >= 1 and codigo_pais_origem <= 3):
    if codigo_produto <= 4:
        preco_total_produto = peso_produto_g * 10
    
    elif codigo_produto <= 7:
        preco_total_produto = peso_produto_g *25
    
    else:
        preco_total_produto =  peso_produto_g * 35
    
    if codigo_pais_origem == 1:
        valor_imposto = preco_total_produto * 0.00

    elif codigo_pais_origem == 2:
        valor_imposto = preco_total_produto * 0.15
    
    else:
        valor_imposto = preco_total_produto * 0.25


    preco_final = preco_total_produto + valor_imposto
    
    # Exibindo resultado
    print("\nPeso do produto convertido em gramas | {:.2f} g".format(peso_produto_g),
    "\nPreço total do produto comprado | R$ {:.2f}".format(preco_total_produto),
    "\nValor do imposto | R$ {:.2f}".format(valor_imposto),
    "\nValor total | R$ {:.2f}".format(preco_final))

else:
    if not(codigo_produto >= 1 and codigo_produto <= 10) and not(codigo_pais_origem >= 1 and codigo_pais_origem <= 3):
        print("\nO código do produto é inválido!")
        print("\nO código do país de origem é inválido!")

    elif not(codigo_pais_origem >= 1 and codigo_pais_origem <= 3):
        print("\nO código do país de origem é inválido!")
    else:
        print("\nO código do produto é inválido!")
