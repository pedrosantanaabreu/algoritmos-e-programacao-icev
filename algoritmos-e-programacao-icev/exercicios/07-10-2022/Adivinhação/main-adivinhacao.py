"""
Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 100, inicialmente, e o usuário tem 5 tentativas para adivinhar o número
OBS.: O design da tela pode ser implementado livremente
Forneça dica se um número informado está no intervalo maior ou menor.
Dica: Use a import random
Implemente um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, receberá a pontuação máxima (ex. 100 pontos); se o usuário adivinhar o número na última tentativa, receberá a pontuação mínima (ex. 10 pontos); se o usuário não acertar o número, não receberá nenhum ponto.
Implemente um controle de erros. Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, o sistema deve notificar o jogador e solicitar o input correto.
Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.
"""
from adivinhacao import JogoAdivinhacao

# Configurações iniciais
jogo_adivinhacao = JogoAdivinhacao()

PONTUACAO_MAXIMA = 100
QUANTIDADE_DE_TENTATIVAS_DO_USUARIO = 5
RANGE_DE_ESCOLHA_DO_COMPUTADOR = (0, 100)

jogo_adivinhacao.definir_pontuacao_maxima(PONTUACAO_MAXIMA)
jogo_adivinhacao.definir_quantidade_de_tentativas_do_usuario(QUANTIDADE_DE_TENTATIVAS_DO_USUARIO)
jogo_adivinhacao.definir_range_de_escolha_do_computador(RANGE_DE_ESCOLHA_DO_COMPUTADOR)
jogo_adivinhacao.definir_tabela_de_pontuacao()

# Iniciando jogo
jogo_adivinhacao.iniciar_jogo()
