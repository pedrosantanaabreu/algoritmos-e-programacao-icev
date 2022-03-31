"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Escreva um programa que leia o valor de 3 ângulos de um triângulo e escreva se o 
triângulo é Acutângulo, Retângulo ou Obtusângulo. Sendo que: − Triângulo Retângulo: possui um 
ângulo reto. (igual a 90o) − Triângulo Obtusângulo: possui um ângulo obtuso. (maior que90o) − 
Triângulo Acutângulo: possui três ângulos agudos. (menor que 90o)
"""

# Recebendo valores
angulo_1 = float(input("1º ângulo | "))
angulo_2 = float(input("2º ângulo | "))
angulo_3 = float(input("3º ângulo | "))

# Calculando
if angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
    print('\nTriângulo Retângulo')

elif angulo_1 == 90 or angulo_2 == 90 or angulo_3 == 90:
    print('\nTriângulo Acutângulo')
    
else:
    print('\nTriângulo Obtusângulo')
