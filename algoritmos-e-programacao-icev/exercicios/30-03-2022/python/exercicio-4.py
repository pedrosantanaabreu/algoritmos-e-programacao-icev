"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um 
fumante perderá. Exiba o total de dias.
"""

# Recebendo valores
cigarros_por_dia = int(input("Digite o consumo de cigarros por dia | "))
anos_fumando = int(input("Digite a quantidade de anos fumando | "))

# Calculando
vida_perdida = cigarros_por_dia * 365 * anos_fumando * 10 / 60 / 24

# Exibindo resultado
print("\nTem de vida perdida | {:.2f} dias".format(vida_perdida))
