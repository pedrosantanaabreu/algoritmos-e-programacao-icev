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
