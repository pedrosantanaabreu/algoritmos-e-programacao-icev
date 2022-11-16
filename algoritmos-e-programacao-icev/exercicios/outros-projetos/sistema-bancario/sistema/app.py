'''
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Sistema de gerenciamento de contas
'''


# Módulos internos
from src import Setup


if __name__ == "__main__":
    try:
        class App:
            def __init__(self) -> None:
                # Verificando todos os arquivos e pendências
                Setup.iniciar_instalacao()

                # Iniciando aplicação
                from src import Main


                Main.iniciar_aplicacao()
        
        
        # Iniciando aplicação
        App()
    except:
        pass
