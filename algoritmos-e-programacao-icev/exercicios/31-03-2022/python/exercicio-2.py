"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa que receba três notas de um aluno,
calcule e mostre a média aritmética e a mensagem constante
na tabela a seguir. Aos alunos que ficaram para exame,
calcule e mostre a nota que deverão tirar para serem
aprovados, considerando que a média exigida é 6,0
"""

# Recebendo valores
nota_l = float(input("Escreva a sua 1º nota | "))
nota_2 = float(input("Escreva a sua 2º nota | "))
nota_3 = float(input("Escreva a sua 3º nota | "))

# Calculando
media = (nota_l + nota_2 + nota_3) / 3 

# Exibindo resultado
print("\nSua média foi {:.1f}".format(media))

if media < 3:
    print("Perdeu playboy! Ficou reprovado.")

elif media >= 3 and media < 7:
    nota_exame = 12 - media
    print("\nFicou de prova final! \n")
    print("Estude para tirar pelo menos {:.1f}".format(nota_exame))

else:
    print("Mandou bem! Passou direto.")
