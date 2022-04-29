"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Faça um programa para ler o código, o sexo (M — masculino; F —
feminino) e o número de horas/aula dadas mensalmente pelos
professores de uma faculdade, sabendo-se que cada hora/aula
vale R$ 50,00. Emita, para cada professor, o código, o salário bruto
e o salário líquido (levando em consideração os descontos
explicados a seguir). Mostre também a média dos salários
líquidos dos professores do sexo masculino e a média dos
salários líquidos dos professores do sexo feminino. Considere:

a) desconto para homens, 10%, e, para mulheres, 5%;

b) as informações terminarão quando for lido o código = 99999
"""

soma_salario_feminino, soma_salario_masculino = 0, 0
contador_feminino, contador_masculino = 0, 0
media_salario_feminino, media_salario_masculino = 0, 0

contador = 1
while True:
    print(f"{'=' * 10} {contador}º Professor {'=' * 10}")

    codigo = int(input("[ ? ] Insira o código | # "))
    if codigo == 99999:
        break

    sexo = input("[ ? ] Digite o sexo (M / F) | ").strip().upper()
    numero_aulas = int(input("[ ? ] Digite o número de aulas / horas | "))

    salario_bruto = numero_aulas * 50
    if sexo == "M":
        salario_liquido = salario_bruto * (1 - 10 / 100)

        contador_masculino += 1
        soma_salario_masculino += salario_liquido
        media_salario_masculino = soma_salario_masculino / contador_masculino

    else:
        salario_liquido = salario_bruto * (1 - 5 / 100)

        contador_feminino += 1
        soma_salario_feminino += salario_liquido
        media_salario_feminino = soma_salario_feminino / contador_feminino

    print(f"\n[ / ] Professor # {codigo}",
    f"\n[ + ] Salário bruto | R$ {salario_bruto:.2f}",
    f"\n[ - ] Descontos | R$ {salario_bruto - salario_liquido:.2f}"
    f"\n[ = ] Salário líquido | R$ {salario_liquido:.2f}\n")

    contador += 1

print(f"\n[ / ] Média dos salários líquidos dos professores do sexo masculino | R$ {media_salario_masculino:.2f}",
f"\n[ / ] Média dos salários líquidos dos professores do sexo feminino | R$ {media_salario_feminino:.2f}")
