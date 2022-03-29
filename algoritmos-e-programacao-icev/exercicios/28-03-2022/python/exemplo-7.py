"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Em uma eleição de líder de turma concorreram ao cargo de presidente três
estudantes (representados pelas variáveis A, B e C). Durante a apuração dos
votos foram computados votos nulos e em branco, além dos votos válidos
para cada candidato. Desenvolva um programa de computador que faça a
leitura da quantidade de votos válidos para cada candidato, além de ler
também a quantidade de votos nulos e em branco. Ao final, o programa deve
apresentar o número total de eleitores, considerando votos válidos, nulos e
em branco; o percentual correspondente de votos válidos em relação à
quantidade de eleitores; o percentual correspondente de votos válidos do
candidato A em relação à quantidade de eleitores; o percentual
correspondente de votos válidos do candidato B em relação à quantidade de
eleitores; o percentual correspondente de votos válidos do candidato C em
relação à quantidade de eleitores; o percentual correspondente de votos
nulos em relação à quantidade de eleitores; e, por último, o percentual
correspondente de votos em branco em relação à quantidade de eleitores.
Todos os cálculos devem efetivamente ser armazenados em memória
"""
	
# Recebendo valores
candidato_a = float(input("Digite a quantidade de votos válidos para o candidato A | "))
candidato_b = float(input("Digite a quantidade de votos válidos para o candidato B | "))
candidato_c = float(input("Digite a quantidade de votos válidos para o candidato C | "))
nulo = float(input("Digite a quantidade de votos nulos | "))
branco = float(input("Digite a quantidade de votos em branco | "))

# Calculando
votos_validos = candidato_a + candidato_b + candidato_c
total_eleitores = votos_validos + nulo + branco

percentual_votos_validos = votos_validos / total_eleitores * 100
percentual_candidato_a = candidato_a / total_eleitores * 100
percentual_candidato_b = candidato_b / total_eleitores * 100
percentual_candidato_c = candidato_c / total_eleitores * 100
percentual_votos_nulos = nulo / total_eleitores * 100
percentual_votos_branco = branco / total_eleitores * 100

# Exibindo resultado
print("""\nNúmero total de eleitores | {:.1f}
Percentual correspondente de votos válidos | {:.1f} %
\nPercentual de votos válidos do candidato A | {:.1f} %
Percentual de votos válidos do candidato B | {:.1f} %
Percentual de votos válidos do candidato C | {:.1f} %
\nPercentual correspondente de votos nulos | {:.1f} %
Percentual correspondente de votos em branco | {:.1f} %"""
.format(total_eleitores,
percentual_votos_validos,
percentual_candidato_a,
percentual_candidato_b,
percentual_candidato_c,
percentual_votos_nulos,
percentual_votos_branco))
