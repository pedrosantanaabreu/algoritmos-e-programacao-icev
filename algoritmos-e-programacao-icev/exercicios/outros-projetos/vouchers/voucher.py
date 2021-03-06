"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@José Cândido

PT-BR:
Sistema de cadastro de contas e vounchers
"""

# Bibliotecas internas
import os
import platform
import time
import ast
import random
import re

# Bibliotecas externas
import pwinput  # pip install pwinput

# Abrindo bando de dados
arquivo = open("banco-de-dados.txt", "a+")
arquivo.close()


"""
- Funções úteis

1. limpar_terminal()
Busca qual o sistema operacional que o computador está usando e usa o comando para limpar o terminal

2. memsagem_carregando()
Recebe como parametro mensagem e segundos
Exibi a mensagem na duração de segundos requirida uma "animação" de carregamento

3. verificar_opcao()
Confere se o input do usuario é equivalente a alguma opção, deve-se passar as opções em formato de lista
"""


def limpar_terminal():
    sistema_operacional = platform.system().upper()

    if sistema_operacional == "WINDOWS":
        os.system("cls")

    else:
        os.system("clear")


def mensagem_carregando(mensagem, segundos):
    for i in range(segundos):
        limpar_terminal()

        if i % 2 == 0:
            print(f"[ / ] {mensagem}")

        else:
            print(f"[ \ ] {mensagem}")

        time.sleep(1)

    limpar_terminal()


def verificar_opcao(input, lista_opcoes):
    for indice, opcao in enumerate(lista_opcoes):
        if str(opcao) == str(input):
            return True

        else:
            if indice == len(lista_opcoes) - 1:
                return False

            else:
                continue


"""
- Menu principal

[ / ] Menu principal

[ 1 ] Entrar
[ 2 ] Registrar
[ 3 ] Sair
[ > ] 

1. Entrar

entrar()
Solicita e-mail e senha e confere se existe no banco de dados
Logo depois confere se a senha inserida é a mesma cadastrada
Caso tudo esteja correto a função direciona o usuario para outro menu
menu_logado()

2. Registrar

registrar()
Solicita o usuario e-mail e senha válidos
Confere se nenhuma conta já foi criada com aquele e-mail
Caso tudo esteja correto, ele envia todos os dados para o banco de dados e volta ao menu_principal


3. Sair

sair()
Exibi uma mensagem de saindo
Fecha o porgrama
"""


def menu_principal():
    lista_opcoes = [1, 2, 3]

    while True:
        limpar_terminal()
        print("[ / ] Menu principal")
        print("\n[ 1 ] Entrar\n[ 2 ] Registrar\n[ 3 ] Sair")
        menu_principal_opcao_usuario = input("[ > ] ").strip()

        if verificar_opcao(menu_principal_opcao_usuario, lista_opcoes):
            menu_principal_opcao_usuario = int(menu_principal_opcao_usuario)

            if menu_principal_opcao_usuario == 1:
                limpar_terminal()
                entrar()

                continue
        
            elif menu_principal_opcao_usuario == 2:
                limpar_terminal()
                registrar()

                continue

            else:
                limpar_terminal()
                sair()

        else:
            mensagem_carregando("Valor inválido, tente novamente", 2)
            continue


"""
- Validadores
"""


def validar_email(email_registrado):
    regex_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex_email, email_registrado):
      return True

    else:
      return False


def validar_senha(senha_registrada):
    if senha_registrada != "":
        return True

    else:
        return False


"""
1. Seção ENTRAR

Futuras atualizaçãos: Seção esqueci a senha
"""


def entrar():
    email_usuario = validar_email_entrar()
    senha_usuario = validar_senha_entrar(email_usuario)

    arquivo = open("banco-de-dados.txt", "r+")

    for conta_registrada in arquivo.readlines():
        lista_conta_registrada = ast.literal_eval(conta_registrada)

        if lista_conta_registrada["email_registrado"] == email_usuario:
            if lista_conta_registrada["senha_registrada"] == senha_usuario:
                menu_logado(lista_conta_registrada)

    arquivo.close()


def validar_email_entrar():
    limpar_terminal()

    while True:
        print("[ / ] Entrar")
        email_registrado = input("\n[ @ ] Digite seu e-mail\n[ > ] ").replace(" ", "").lower()

        if validar_email(email_registrado) and conferir_email_banco_de_dados(email_registrado):
            return email_registrado

        else:
            mensagem_carregando("Valor inválido ou e-mail não cadastrado, tente novamente", 2)
            continue


def validar_senha_entrar(email_usuario):
    limpar_terminal()

    while True:
        print("[ / ] Entrar")
        senha_usuario = pwinput.pwinput("\n[ ? ] Digite sua senha\n[ > ] ").replace(" ", "")

        arquivo = open("banco-de-dados.txt", "r+")

        for conta_registrada in arquivo.readlines():
            lista_conta_registrada = ast.literal_eval(conta_registrada)

            if lista_conta_registrada["email_registrado"] == email_usuario:
                if lista_conta_registrada["senha_registrada"] == senha_usuario:
                    return senha_usuario

                else:
                    mensagem_carregando("Senha inválida, tente novamente", 2)
                    continue


"""
2. Seção REGISTRAR
"""


def registrar():
    email_registrado = registrar_email()
    senha_registrada = registrar_senha()
    vouchers = []

    conta_registrada = {
        "email_registrado" : email_registrado,
        "senha_registrada" : senha_registrada,
        "vouchers" : vouchers
    }

    mensagem_carregando("Estamos armazenando seus dados", 2)

    armazenar_no_banco_de_dados(conta_registrada)

    mensagem_carregando("Conta registrada com sucesso", 2)


def conferir_email_banco_de_dados(email_registrado):
    with open("banco-de-dados.txt", 'r') as f:
        texto = f.readlines()

    for dicionario in texto:
        dicionario = ast.literal_eval(dicionario)

        if email_registrado == dicionario["email_registrado"]:
            return True

    return False
    

def registrar_email():
    limpar_terminal()

    while True:
        print("[ / ] Registrar")
        email_registrado = input("\n[ @ ] Digite seu e-mail\n[ > ] ").replace(" ", "").lower()

        if validar_email(email_registrado) and not conferir_email_banco_de_dados(email_registrado):
            return email_registrado

        else:
            mensagem_carregando("E-mail inválido ou já cadastrado, tente novamente", 2)
            continue


def registrar_senha():
    limpar_terminal()

    while True:
        print("[ / ] Registrar")
        senha_registrada = pwinput.pwinput("\n[ ? ] Digite sua senha\n[ > ] ").strip()

        if validar_senha(senha_registrada):
            return senha_registrada

        else:
            mensagem_carregando("Senha inválida, tente novamente", 2)
            continue




def armazenar_no_banco_de_dados(conta_registrada):
    arquivo = open("banco-de-dados.txt", "a+")
    arquivo.write(str(conta_registrada) + "\n")
    arquivo.close()


"""
3. Seção SAIR
"""


def sair():
    mensagem_carregando("Saindo", 2)
    exit()


"""
- Menu Logado

[ / ] Menu logado

[ 1 ] Criar voucher
[ 2 ] Ver meus vouchers
[ 3 ] Desconectar

1. Criar voucher

criar_voucher()
Cria uma sequencia de 3 letras no inicio e 3 numeros no final
Depois de criado, precisamos adicionar o voucher no banco de dados
Para isso o programa remove os dados anteriores no banco de dados e sobre escreve os novos

2. Ver meus vouchers

ver_vouchers()
Deve ser passado o dicionario contendo os dados do cliente
O programa busca no banco de dados alguma conta com o e-mail do usuario
Caso encontre, retorna o lista contendo os vouchers

3. Desconectar
Manda o usuario novamente ao menu principal

Futuras atualizações:
Mudar E-mail cadastrado
Mudar senha cadastrada
Remover vouchers
"""


def menu_logado(lista_conta_registrada):
    lista_opcoes = [1, 2, 3]

    while True:
        limpar_terminal()
        print("[ / ] Menu logado")
        print(f'\n[ / ] Bem-vindo(a) {lista_conta_registrada["email_registrado"]}\n',
        "\n[ 1 ] Criar voucher",
        "\n[ 2 ] Ver meus vouchers",
        "\n[ 3 ] Desconectar")
        menu_logado_opcao_usuario = input("[ > ] ").strip()

        if verificar_opcao(menu_logado_opcao_usuario, lista_opcoes):
            menu_logado_opcao_usuario = int(menu_logado_opcao_usuario)

            if menu_logado_opcao_usuario == 1:
                voucher = criar_voucher()
                adicionar_voucher_no_banco_de_dados(voucher, lista_conta_registrada)

                continue
        
            elif menu_logado_opcao_usuario == 2:
                limpar_terminal()

                ver_vouchers(lista_conta_registrada)
                continuar_input = input("[ Enter ] Para continuar\n")

                continue

            else:
                mensagem_carregando("Desconectando", 2)
                menu_principal()

        else:
            mensagem_carregando("Valor inválido, tente novamente", 2)
            continue


"""
1. Seção CRIAR VOUCHER
"""


def criar_voucher():
    """
    Voucher = 3 letras no inicio e 3 numeros no final
    """

    voucher = ""
    numeros = "0123456789"
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(6):
        if i < 3:
            voucher += caracteres[random.randint(0, len(caracteres) - 1)]
        else:
            voucher += numeros[random.randint(0, len(numeros) - 1)]

    mensagem_carregando("Criando voucher", 2)
    print(f"Voucher criado com sucesso | {voucher}")

    continuar_input = input("\n[ Enter ] Para continuar\n")

    return voucher


def adicionar_voucher_no_banco_de_dados(voucher, conta_logada):
    email_registrado = conta_logada["email_registrado"]
    senha_registrada = conta_logada["senha_registrada"]
    

    with open("banco-de-dados.txt", 'r') as f:
        texto = f.readlines()

    for dicionario in texto:
        dicionario = ast.literal_eval(dicionario)

        if email_registrado == dicionario["email_registrado"]:
            vouchers = list(dicionario["vouchers"])
            vouchers.append(voucher)

    conta_atualizada = {
        "email_registrado" : email_registrado,
        "senha_registrada" : senha_registrada,
        "vouchers" : vouchers
    }

    arquivo = open("banco-de-dados.txt", "r+")

    index_linha = 0
    for linha in arquivo:
        index_linha += 1

        if str(conta_logada) + "\n" in linha:
            break

    arquivo.close()
    atualizar_linha(index_linha, str(conta_atualizada) + "\n")


def atualizar_linha(numero_linha_deletar, novo_cadastro):
    with open("banco-de-dados.txt", 'r') as f:
        texto = f.readlines()

    with open("banco-de-dados.txt", 'w') as f:
        contador = 0
        for i in texto:
            contador += 1

            if contador == numero_linha_deletar:
                f.write(novo_cadastro)

            else:
                f.write(i)


"""
2. Seção VER VOUCHERS
"""


def ver_vouchers(conta_logada):
    limpar_terminal()

    email_registrado = conta_logada["email_registrado"]

    with open("banco-de-dados.txt", 'r') as f:
        texto = f.readlines()
    for dicionario in texto:
        dicionario = ast.literal_eval(dicionario)

        if email_registrado == dicionario["email_registrado"]:
            contador_vouchers = 0
            for indice, voucher in enumerate(dicionario["vouchers"]):
                contador_vouchers += 1
                print('-' * 10)
                print(f"| {voucher} | --- {indice + 1}º")
                print('-' * 10)

            if contador_vouchers != 0:
                print()


"""
- Função principal
"""


def principal():
    menu_principal()


principal()
