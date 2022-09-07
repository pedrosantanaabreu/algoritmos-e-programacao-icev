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
lista = [print('\033c', end=''), [print('[ 1 ] Incluir aluno\n[ 2 ] Incluir nota do aluno\n[ 3 ] Lista alunos e notas\n[ 4 ] Sair do programa')], lambda *args: [print(f'[ {index + 5} ] {valor}') if args else print() for index, valor in enumerate(args)]]
