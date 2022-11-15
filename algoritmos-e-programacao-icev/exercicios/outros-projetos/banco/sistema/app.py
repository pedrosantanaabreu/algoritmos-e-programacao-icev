if __name__ == '__main__':
    from src import Setup, Main


    class App:
        def __init__(self):
            Setup.iniciar_instalacao()
            Main.iniciar_aplicacao()


    App()
