import time

PALAVRA_SECRETA = 'QWERTYUIOPASDFGHJKLZXCVBNM' * 5000
palavra_secreta_display = ['_'] * len(PALAVRA_SECRETA)


def atualizar_estado_atual_da_palavra_secreta_1(letra_digitada_pelo_usuario):
    global PALAVRA_SECRETA
    global palavra_secreta_display
    for letra_index in range(len(PALAVRA_SECRETA)):
        if letra_digitada_pelo_usuario == PALAVRA_SECRETA[letra_index]:
            palavra_secreta_display[letra_index] = letra_digitada_pelo_usuario
        else:
            pass


def atualizar_estado_atual_da_palavra_secreta_2(letra_digitada_pelo_usuario):
    global PALAVRA_SECRETA
    global palavra_secreta_display
    index_proprio = PALAVRA_SECRETA.find(letra_digitada_pelo_usuario) - 1
    for _ in range(PALAVRA_SECRETA.count(letra_digitada_pelo_usuario)):
        palavra_secreta_display[PALAVRA_SECRETA.find(letra_digitada_pelo_usuario, index_proprio + 1)] = letra_digitada_pelo_usuario
        index_proprio = PALAVRA_SECRETA.find(letra_digitada_pelo_usuario, index_proprio + 1)


tempo_1 = []
for _ in range(10):
    inicio_1 = time.time()
    for letra in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        atualizar_estado_atual_da_palavra_secreta_1(letra)
    fim_1 = time.time()
    tempo_1.append(fim_1 - inicio_1)


tempo_2 = []
for _ in range(10):
    inicio_2 = time.time()
    for letra in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        atualizar_estado_atual_da_palavra_secreta_2(letra)
    fim_2 = time.time()
    tempo_2.append(fim_2 - inicio_2)


print(f'[ - ] 1ª função\n[ - ] Tempo total | {sum(tempo_1):.2f} segundos\n[ - ] Media | {sum(tempo_1) / len(tempo_1):.2f} segundos\n')
print(f'[ - ] 2ª função\n[ - ] Tempo total | {sum(tempo_2):.2f} segundos\n[ - ] Media | {sum(tempo_2) / len(tempo_2):.2f} segundos')
