'''
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
1. Desenvolva um algoritmo que receba como parâmetro um número binário e retorne
o número decimal equivalente.

2. Desenvolva um algoritmo que receba como parâmetro um número hexadecimal e
retorne o número decimal equivalente.

3. Desenvolva um algoritmo que receba como parâmetro um número decimal e retorne
o número binário equivalente.
'''
numero_convertido = 0
hexadecimal_tabela = '0123456789ABCDEF'

while True:
    base_principal = input('Converter de:\n1. Binário\n2. Decimal\n3. Hexadecimal\n-> ').strip()
    base_conversao = input('\nPara:\n1. Binário\n2. Decimal\n3. Hexadecimal\n-> ').strip()

    if not (base_principal == '1' or base_principal == '2' or base_principal == '3') or not (base_conversao == '1' or base_conversao == '2' or base_conversao == '3'):
        print('\n[ ! ] Um dos valor digitados é inváido, tente novamente:')
        continue
    else:
        numero_para_conversao = input('\nDigite o número para conversão | ')
        break

if base_principal == '1':
    if base_conversao == '1':
        numero_convertido = numero_para_conversao

    elif base_conversao == '2':
        i = 0
        for numero_binario in numero_para_conversao:
            numero_convertido += int(numero_binario) * 2 ** i
            i += 1

    else:
        numero_convertido = ''
        for i in range(0, len(numero_para_conversao), 4):
            resultado_conversao_bloco_binario_hexadecimal = 0
            bloco = numero_para_conversao[-4 - i:len(numero_para_conversao) - i]

            for j in range(len(bloco)):
                resultado_conversao_bloco_binario_hexadecimal += int(bloco[len(bloco) - 1 - j]) * 2 ** j

            numero_convertido += hexadecimal_tabela[resultado_conversao_bloco_binario_hexadecimal]
        numero_convertido = numero_convertido[::-1]

elif base_principal == '2':
    if base_conversao == '1':
        numero_convertido = ''
        while True:
            divisao_inteira_decimal_binario = int(numero_para_conversao) // 2
            resto_divisao_decimal_binario = int(numero_para_conversao) % 2
            numero_convertido += str(resto_divisao_decimal_binario)
            numero_para_conversao = divisao_inteira_decimal_binario

            if divisao_inteira_decimal_binario == 0:
                numero_convertido = numero_convertido[::-1]
                break

    elif base_conversao == '2':
        numero_convertido = numero_para_conversao

    else:
        print()

else:
    print()
print(numero_convertido)
