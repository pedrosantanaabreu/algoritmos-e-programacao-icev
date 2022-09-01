# Tipos de matrizes
def matriz_linha(matriz):
    if len(matriz) == 1:
        return True
    else:
        return False


def matriz_coluna(matriz):
    if len(matriz[0]) == 1:
        return True
    else:
        return False


def matriz_nula(matriz):
    for linha in matriz:
        if linha.count(0) != len(linha):
            return False
    return True


def matriz_quadrada(matriz):
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False


def matriz_diagonal(matriz):
    for diagonal in range(len(matriz)):
        if matriz[diagonal][diagonal] == 0 or matriz[diagonal].count(0) != len(matriz) - 1:
            return False
        else:
            return True


print(matriz_diagonal([[1, 0], [0, 1]]))
