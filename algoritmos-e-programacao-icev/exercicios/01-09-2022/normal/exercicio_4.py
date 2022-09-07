"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Crie um programa para apresentar um menu de opções, conforme o layout a
seguir:
1. Incluir aluno
2. Incluir nota do aluno
3. Lista Alunos e Notas
4. Sair do programa
Crie uma função para definir um item do menu
Crie uma função para apresentar o menu
Crie uma função para limpar a tela sempre que o menu for apresentado
"""
from os import system as os_system


def limpar_terminal():
    os_system('cls||clear') 


def imprimir_menu():
    limpar_terminal()

    print('[ 1 ] Incluir aluno\n' +
    '[ 2 ] Incluir nota do aluno\n' +
    '[ 3 ] Lista alunos e notas\n' +
    '[ 4 ] Sair do programa')


def definir_itens_menu(*args):
    if args:
        for index, valor in enumerate(args):
            print(f'[ {index + 5} ] {valor}')
