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
                if not i in '0123456789ABCDEF':
                    verificador = False
                    print('\n[ ! ] O valor digitado é inváido, tente novamente:')
                    break
                else:
                    verificador = True
            if verificador:
                break
        break    
    print('\n[ ! ] Um dos valor digitados é inváido, tente novamente:\n')

if base_principal == base_conversao:
    numero_convertido = numero_para_conversao

elif base_principal == '1':
    if base_conversao == '2':
        for i in range(len(numero_para_conversao)):
                numero_convertido += int(numero_para_conversao[len(numero_para_conversao) - 1 - i]) * 2 ** i
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
            if resto_divisao_decimal_binario == '10':
                letra_numero_hexadecimal = 'A'
            elif resto_divisao_decimal_binario == '11':
                letra_numero_hexadecimal = 'B'
            elif resto_divisao_decimal_binario == '12':
                letra_numero_hexadecimal = 'C'
            elif resto_divisao_decimal_binario == '13':
                letra_numero_hexadecimal = 'D'
            elif resto_divisao_decimal_binario == '14':
                letra_numero_hexadecimal = 'E'
            else:
                letra_numero_hexadecimal = 'F'

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
            index_hexadecimal = int(hexadecimal_tabela.index(i))
            while True:
                divisao_inteira_decimal_binario = int(index_hexadecimal) // 2
                resto_divisao_decimal_binario = int(index_hexadecimal) % 2
                numero_convertido += str(resto_divisao_decimal_binario)
                index_hexadecimal = divisao_inteira_decimal_binario

                if divisao_inteira_decimal_binario == 0:
                    break

        numero_convertido = numero_convertido[::-1]
    
    else:
        for i in range(len(numero_para_conversao)):
            numero_convertido += 16 ** i * hexadecimal_tabela.index(str(numero_para_conversao[len(numero_para_conversao) - 1 - i]))

print(f'\n[ / ] {escolha_numero_principal} | {numero_para_conversao}\n[ / ] {escolha_numero_conversao} | {numero_convertido}')
