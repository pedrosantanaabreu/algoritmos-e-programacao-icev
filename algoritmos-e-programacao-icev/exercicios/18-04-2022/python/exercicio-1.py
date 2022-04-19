'''
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Uma empresa decidiu fazer um levantamento em relação aos
candidatos que se apresentarem para preenchimento de vagas em seu
quadro de funcionários. Supondo que você seja o programador dessa
empresa, faça um programa que leia a quantidade de candidatos que se
apresentaram e, para cada um, leia a idade, o sexo (M ou F) e a
experiência no serviço (S ou N). O programa deve calcular e mostrar:

a) o número de candidatos do sexo feminino;

b) o número de candidatos do sexo masculino;

c) a idade média dos homens que já têm experiência no serviço;

d) a porcentagem dos homens com mais de 45 anos entre o total dos
homens;

e) o número de mulheres com idade inferior a 21 anos e com experiência
no serviço;

f) a menor idade entre as mulheres que já têm experiência no serviço.
'''

quantidade_feminino = 0
feminino_menor_21_anos_com_experiencia = 0
feminino_menor_idade_experiencia = 0

quantidade_masculino = 0
soma_idade_masculino_experiencia = 0
quantidade_masculino_experiencia = 0
masculino_maior_45_anos = 0
porcentagem_masculino_45_anos = 0
idade_media_masculino_experiencia= 0

numero_candidatos = int(input('Digite o número de candidatos | '))

for i in range(1, numero_candidatos + 1):
    while True:
        print(f'\n[ + ] {i}º candidato\n{"-=" * 30}')
        idade = input(f'Digite a idade | ').strip().upper()
        sexo = input(f'Digite o sexo (M / F) | ').strip().upper()
        experiencia_servico = input(f'Digite se tem experiência no serviço (S ou N) | ').strip().upper()
        
        if (idade.isnumeric() and idade > 0) and (sexo == 'M' or sexo == 'F') and (experiencia_servico == 'S' and experiencia_servico == 'N'):
            break

    if sexo == 'M':
        quantidade_masculino += 1

        if idade > 45:
            masculino_maior_45_anos += 1

        if experiencia_servico == 'S':
            quantidade_masculino_experiencia += 1
            soma_idade_masculino_experiencia += idade
    else:
        quantidade_feminino += 1

        if idade < 21 and experiencia_servico == 'S':
            if idade < feminino_menor_idade_experiencia:
                feminino_menor_idade_experiencia = idade
            else:
                feminino_menor_idade_experiencia = idade

            feminino_menor_21_anos_com_experiencia += 1
        
if quantidade_masculino_experiencia != 0:
    idade_media_masculino_experiencia = soma_idade_masculino_experiencia / quantidade_masculino_experiencia

if masculino_maior_45_anos != 0:
    porcentagem_masculino_45_anos = quantidade_masculino / masculino_maior_45_anos

print(f'''
O número de candidatos do sexo feminino | {quantidade_feminino}
O número de candidatos do sexo masculino | {quantidade_masculino}

Idade média dos homens que já têm experiência no serviço | {idade_media_masculino_experiencia:.2f}
Porcentagem dos homens com mais de 45 anos entre o total dos homens | {porcentagem_masculino_45_anos:.2f} %
Número de mulheres com idade inferior a 21 anos e com experiência no serviço | {feminino_menor_21_anos_com_experiencia}
Menor idade entre as mulheres que já têm experiência no serviço | {feminino_menor_idade_experiencia}
''')
