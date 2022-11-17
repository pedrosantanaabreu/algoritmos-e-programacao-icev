'''
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Sistema de gerenciamento de contas
'''


if __name__ == "__main__":
    try:
        from src import Setup
    except:
        import os
        
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print('Certifique-se que todos os arquivos estão no projeto.')
        exit()


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
