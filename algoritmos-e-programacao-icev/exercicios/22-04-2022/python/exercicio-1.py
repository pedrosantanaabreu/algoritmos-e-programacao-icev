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
        while True:
            numero_para_conversao = input('\nDigite o número para conversão | ').strip().upper()
            for i in numero_para_conversao:
                if not i in '123456789ABCDEF':
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

    else:
        numero_convertido = ''
        while True:
            divisao_inteira_decimal_binario = int(numero_para_conversao) // 16
            resto_divisao_decimal_binario = int(numero_para_conversao) % 16
            numero_convertido += hexadecimal_tabela[resto_divisao_decimal_binario]
            numero_para_conversao = divisao_inteira_decimal_binario

            if divisao_inteira_decimal_binario == 0:
                numero_convertido = numero_convertido[::-1]
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

print(f'\nO número {numero_para_conversao} convertido fica {numero_convertido}')
