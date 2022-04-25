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
hexadecimal_tabela = '0123456789ABCDEF'
escolhas = ['Binário','Decimal', 'Hexadecimal']

# Recebe Int e retorna Int
def converter_binario_para_binario(numero_para_converter):
    return numero_para_converter

# Recebe Int e retorna Int
def converter_binario_para_decimal(numero_para_converter):
    numero_para_converter = str(numero_para_converter)
    resultado_binario_para_decimal = 0

    for i in range(len(numero_para_converter)):
        resultado_binario_para_decimal += int(numero_para_converter[len(numero_para_converter) - 1 - i]) * 2 ** i

    return int(resultado_binario_para_decimal)

# Recebe Int e retorna String
def converter_binario_para_hexadecimal(numero_para_converter):
    numero_para_converter = str(numero_para_converter)
    resultado_binario_para_hexadecimal = ''

    for i in range(0, len(numero_para_converter), 4):
        resultado_binario_para_hexadecimal += hexadecimal_tabela[converter_binario_para_decimal(numero_para_converter[-4 - i:len(numero_para_converter) - i])]
    
    return resultado_binario_para_hexadecimal[::-1]

# Recebe Int e retorna Int
def converter_decimal_para_decimal(numero_para_converter):
    return numero_para_converter

# Recebe Int e retorna Int
def converter_decimal_para_binario(numero_para_converter):
    resultado_decimal_para_binario = ''

    while numero_para_converter != 0:
        resultado_decimal_para_binario += str(int(numero_para_converter) % 2)
        numero_para_converter //= 2

    return resultado_decimal_para_binario[::-1] or 0

# Recebe Int e retorna String
def converter_decimal_para_hexadecimal(numero_para_converter):
    resultado_decimal_para_binario = ''

    while numero_para_converter != 0:
        resultado_decimal_para_binario += hexadecimal_tabela[numero_para_converter % 16]
        numero_para_converter //= 16

    return resultado_decimal_para_binario[::-1] or 0

# Recebe String ou Int e retorna String
def converter_hexadecimal_para_hexadecimal(numero_para_converter):
    return numero_para_converter

# Recebe String ou Int e retorna Int
def converter_hexadecimal_para_decimal(numero_para_converter):
    numero_para_converter = str(numero_para_converter)
    resultado_hexadecimal_para_decimal = 0

    for i in range(len(numero_para_converter)):
        resultado_hexadecimal_para_decimal += hexadecimal_tabela.index(str(numero_para_converter[len(numero_para_converter) - 1 - i])) * 16 ** i
    
    return int(resultado_hexadecimal_para_decimal)

# Recebe String ou Int e retorna Int
def converter_hexadecimal_para_binario(numero_para_converter):
    numero_para_converter = str(numero_para_converter)
    resultado_hexadecimal_para_binario = ''

    for i in numero_para_converter:
        print(resultado_hexadecimal_para_binario)
        resultado_hexadecimal_para_binario += str(converter_decimal_para_binario(int(hexadecimal_tabela.index(i))))

    return int(resultado_hexadecimal_para_binario) or 0

# Main
def inicio():
    while True:
        while True:
            base_principal = input('[ ? ] De:\n[ 1 ] Binário\n[ 2 ] Decimal\n[ 3 ] Hexadecimal\n[ > ] ').strip()
            base_conversao = input('\n[ ? ] Para:\n[ 1 ] Binário\n[ 2 ] Decimal\n[ 3 ] Hexadecimal\n[ > ] ').strip()

            if base_principal in '123' and base_conversao in '123':
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

        if base_principal == '1':
            if base_conversao == '1':
                numero_convertido = converter_binario_para_binario(int(numero_para_conversao))
            elif base_conversao == '2':
                numero_convertido = converter_binario_para_decimal(int(numero_para_conversao))
            else:
                numero_convertido = converter_binario_para_hexadecimal(int(numero_para_conversao))

        elif base_principal == '2':
            if base_conversao == '1':
                numero_convertido = converter_decimal_para_binario(int(numero_para_conversao))
            elif base_conversao == '2':
                numero_convertido = converter_decimal_para_decimal(int(numero_para_conversao))
            else:
                numero_convertido = converter_decimal_para_hexadecimal(int(numero_para_conversao))

        else:
            if base_conversao == '1':
                numero_convertido = converter_hexadecimal_para_binario(numero_para_conversao)
            elif base_conversao == '2':
                numero_convertido = converter_hexadecimal_para_decimal(numero_para_conversao)
            else:
                numero_convertido = converter_hexadecimal_para_hexadecimal(numero_para_conversao)

        print(f'\n[ / ] {escolhas[int(base_principal) - 1]} | {numero_para_conversao}\n[ / ] {escolhas[int(base_conversao) - 1]} | {numero_convertido}')

        while True:
            resposta_continuar_sair = input('\n[ 1 ] Converter outro número\n[ 2 ] Sair\n[ > ] ').strip()

            if resposta_continuar_sair == '1':
                verificador_continuar = True
                break
            elif resposta_continuar_sair == '2':
                verificador_continuar = False
                break
            else:
                print('[ ! ] O valor digitado é inváido, tente novamente:')

        if not verificador_continuar:
            break
    print('\n[ / ] Programa finalizado com êxito')

inicio()
