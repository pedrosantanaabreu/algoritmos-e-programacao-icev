"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa para efetuar o cálculo da quantidade de litros de
combustível gasta em uma viagem, considerando um automóvel que faz 12
Km/l. Para obter o cálculo, o usuário deve fornecer o tempo gasto (variável
TEMPO) e a velocidade média (variável VELOCIDADE) durante a viagem.
Dessa forma, será possível obter a distância percorrida com a fórmula
DISTÂNCIA = TEMPO * VELOCIDADE. A partir do valor da distância, basta
calcular a quantidade de litros de combustível utilizada na viagem com a
fórmula LITROS_USADOS = DISTÂNCIA / 12. O programa deve apresentar
os valores da velocidade média, tempo gasto na viagem, a distância
percorrida e a quantidade de litros utilizada na viagem.
"""

# Recebendo valores
tempo = float(input("Digite o tempo gasto em horas | "))
velocidade = float(input("Digite a velocidade média em Km/h | "))

# Calculando
distancia = tempo * velocidade
litros_usados = distancia / 12

# Exibindo resultado
print("""\nVelocidade média | {:.2f} Km/h
Tempo gasto na viagem | {:.1f} Hrs
Distância percorrida | {:.2f} Km
Quantidade de litros utilizada na viagem | {:.1f} L""".format(velocidade, tempo, distancia, litros_usados))
