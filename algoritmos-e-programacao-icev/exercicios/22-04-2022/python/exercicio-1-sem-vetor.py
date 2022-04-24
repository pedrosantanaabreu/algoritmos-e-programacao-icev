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
    base_principal = input('[ ? ] De:\n[ 1 ] Binário\n[ 2 ] Decimal\n[ 3 ] Hexadecimal\n[ > ] ').strip()
    base_conversao = input('\n[ ? ] Para:\n[ 1 ] Binário\n[ 2 ] Decimal\n[ 3 ] Hexadecimal\n[ > ] ').strip()

    if base_principal in '123' and base_conversao in '123':
        if base_principal == '1':
            escolha_numero_principal = 'Binário'
        elif base_principal == '2':
            escolha_numero_principal = 'Decimal'
        else:
            escolha_numero_principal = 'Hexadecimal'

        if base_conversao == '1':
            escolha_numero_conversao = 'Binário'
        elif base_conversao == '2':
            escolha_numero_conversao = 'Decimal'
        else:
            escolha_numero_conversao = 'Hexadecimal'

        while True:
            numero_para_conversao = input('\n[ ? ] Digite o número para conversão\n[ > ] ').strip().upper()

            for i in numero_para_conversao:
                if base_principal == '1' and i in '01' or base_principal == '2' and i in '0123456789' or base_principal == '3' and i in '0123456789ABCDEF':
                    verificador = True
                else:
                    verificador = False
                    break
    
            if verificador:
                break
            print('\n[ ! ] O valor digitado é inváido, tente novamente:')
        break
    print('\n[ ! ] Um dos valor digitados é inváido, tente novamente:\n')

if base_principal == base_conversao:
    numero_convertido = numero_para_conversao

elif base_principal == '1':
    if base_conversao == '2':
        numero_invertido_binario = ''
        for i in numero_para_conversao:
            numero_invertido_binario = i + numero_invertido_binario

        potencia = 0
        while True:
            for j in numero_invertido_binario:
                numero_convertido += int(j) * 2 ** potencia
                potencia += 1
            break
    else:
        numero_convertido = ''
        for i in range(0, len(numero_para_conversao), 4):
            resultado_conversao_bloco_binario_hexadecimal = 0
            bloco = numero_para_conversao[-4 - i:len(numero_para_conversao) - i]

            bloco_invertido = bloco
            bloco = ''
            for j in bloco_invertido:
                bloco = j + bloco

            potencia = 0
            resultado_conversao_bloco_binario_hexadecimal = 0
            while True:
                for k in bloco:
                    resultado_conversao_bloco_binario_hexadecimal += int(k) * 2 ** potencia
                    potencia += 1
                break

            if resultado_conversao_bloco_binario_hexadecimal > 9:
                    if resultado_conversao_bloco_binario_hexadecimal == 10:
                        numero_binario_hexadecimal = 'A'
                    elif resultado_conversao_bloco_binario_hexadecimal == 11:
                        numero_binario_hexadecimal = 'B'
                    elif resultado_conversao_bloco_binario_hexadecimal == 12:
                        numero_binario_hexadecimal = 'C'
                    elif resultado_conversao_bloco_binario_hexadecimal == 13:
                        numero_binario_hexadecimal = 'D'
                    elif resultado_conversao_bloco_binario_hexadecimal == 14:
                        numero_binario_hexadecimal = 'E'
                    else:
                        numero_binario_hexadecimal = 'F'
            else:
                numero_binario_hexadecimal = str(resultado_conversao_bloco_binario_hexadecimal)
    
            numero_convertido += numero_binario_hexadecimal

        binario_hexadecimal_invertido = numero_convertido
        numero_convertido = ''
        for i in binario_hexadecimal_invertido:
            numero_convertido = i + numero_convertido

elif base_principal == '2':
    numero_convertido = ''
    dividendo = numero_para_conversao

    if base_conversao == '1':
        divisor = 2
    else:
        divisor = 16

    while True:
        divisao_inteira_decimal_binario = int(dividendo) // divisor
        resto_divisao_decimal_binario = int(dividendo) % divisor

        if divisor == 16:
            if resto_divisao_decimal_binario > 9:
                if resto_divisao_decimal_binario == 10:
                    letra_numero_hexadecimal = 'A'
                elif resto_divisao_decimal_binario == 11:
                    letra_numero_hexadecimal = 'B'
                elif resto_divisao_decimal_binario == 12:
                    letra_numero_hexadecimal = 'C'
                elif resto_divisao_decimal_binario == 13:
                    letra_numero_hexadecimal = 'D'
                elif resto_divisao_decimal_binario == 14:
                    letra_numero_hexadecimal = 'E'
                else:
                    letra_numero_hexadecimal = 'F'
            else:
                letra_numero_hexadecimal = str(resto_divisao_decimal_binario)

            numero_convertido += letra_numero_hexadecimal
        else:
            numero_convertido += str(resto_divisao_decimal_binario)
        dividendo = divisao_inteira_decimal_binario

        if divisao_inteira_decimal_binario == 0:
            numero_invertido_decimal = numero_convertido
            numero_convertido = ''
            for i in numero_invertido_decimal:
                numero_convertido = i + numero_convertido
            break

else:
    if base_conversao == '1':
        numero_convertido = ''
        for i in numero_para_conversao:
            if i == 'A':
                numero_hexadecimal_binario = 10
            elif i == 'B':
                numero_hexadecimal_binario = 11
            elif i == 'C':
                numero_hexadecimal_binario = 12
            elif i == 'D':
                numero_hexadecimal_binario = 13
            elif i == 'E':
                numero_hexadecimal_binario = 14
            elif i == 'F':
                numero_hexadecimal_binario = 15
            else:
                numero_hexadecimal_binario = i

            while True:
                divisao_inteira_decimal_binario = int(numero_hexadecimal_binario) // 2
                resto_divisao_decimal_binario = int(numero_hexadecimal_binario) % 2
                numero_convertido += str(resto_divisao_decimal_binario)
                numero_hexadecimal_binario = divisao_inteira_decimal_binario

                if divisao_inteira_decimal_binario == 0:
                    break

        numero_invertido_hexadecimal_binario = ''
        for i in numero_convertido:
            numero_invertido_hexadecimal_binario = i + numero_invertido_hexadecimal_binario
        numero_convertido = numero_invertido_hexadecimal_binario

    else:
        numero_invertido_hexadecimal_decimal = ''
        for i in numero_para_conversao:
            numero_invertido_hexadecimal_decimal = i + numero_invertido_hexadecimal_decimal

        potencia = 0
        while True:
            for i in numero_invertido_hexadecimal_decimal:
                if i == 'A':
                    j = 10
                elif i == 'B':
                    j = 11
                elif i == 'C':
                    j = 12
                elif i == 'D':
                    j = 13
                elif i == 'E':
                    j = 14
                elif i == 'F':
                    j = 15
                else:
                    j = i

                numero_convertido += int(j) * 16 ** potencia 
                potencia += 1
            break

print(f'\n[ / ] {escolha_numero_principal} | {numero_para_conversao}\n[ / ] {escolha_numero_conversao} | {numero_convertido}')
