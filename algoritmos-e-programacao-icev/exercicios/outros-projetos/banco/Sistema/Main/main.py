import importlib.util


class Main():
    def __init__(self):
        self.__importar_modulos()


    def __importar_modulo(self, nome, caminho):
        localizacao = importlib.util.spec_from_file_location(nome, caminho)
        modulo = importlib.util.module_from_spec(localizacao)
        localizacao.loader.exec_module(modulo)

        return modulo


    def __importar_modulos(self):
        self.__utilitarios = self.__importar_modulo('utilitarios', 'Sistema\\Utilitarios\\utilitarios.py')
        self.__interfaces = self.__importar_modulo('interfaces', 'Sistema\\Interfaces\\interfaces.py')
        self.__validadores = self.__importar_modulo('validadores', 'Sistema\\Utilitarios\\validadores.py')
        self.__dados = self.__importar_modulo('dados', 'Sistema\\Dados\\dados.py')


    # Main
    def iniciar(self):
        while True:
            self.__utilitarios.Utilitarios.limpar_terminal()
            self.__interfaces.Interfaces.imprimir_menu_principal()
            opcao_menu_principal = input('| -> ')

            if self.__validadores.Validadores.validar_opcao_menu(5, opcao_menu_principal):
                self.__chamar_opcoes(opcao_menu_principal)
            else:
                self.__utilitarios.Utilitarios.mensagem_de_erro(f'O valor "{opcao_menu_principal}" é inválido.')

    # Principal
    def __chamar_opcoes(self, opcao):
        opcao = int(opcao)

        if opcao == 1:
            self.__opcao_adicionar()
        elif opcao == 2:
            ...
        elif opcao == 3:
            ...
        elif opcao == 4:
            ...
        else:
            self.__opcao_sair()
    

    # Adicionar
    def __opcao_adicionar(self):
        while True:
            self.__utilitarios.Utilitarios.limpar_terminal()
            self.__interfaces.Interfaces.imprimir_menu_adicionar()
            opcao_menu_adicionar = input('| -> ')
        
            if self.__validadores.Validadores.validar_opcao_menu(3, opcao_menu_adicionar):
                if int(opcao_menu_adicionar) == 3:
                    break

                self.__chamar_opcoes_menu_adicionar(opcao_menu_adicionar)
                
            else:
                self.__utilitarios.Utilitarios.mensagem_de_erro(f'O valor "{opcao_menu_adicionar}" é inválido.')


    def __chamar_opcoes_menu_adicionar(self, opcao_menu_adicionar):
        opcao_menu_adicionar = int(opcao_menu_adicionar)
        if opcao_menu_adicionar == 1:
            self.__adicionar_cliente()
        else:
            self.__adicionar_conta()


    def __obter_nome_cliente(self):
        while True:
                self.__utilitarios.Utilitarios.limpar_terminal()
                self.__interfaces.Interfaces.imprimir_menu('Adicionando Cliente', 'Adicionando Cliente')
                self.__interfaces.Interfaces.imprimir_menu('Informe o nome do cliente', 'Informe o nome do cliente', ['Voltar'])
                nome_cliente = input('| -> ').strip().title()

                if nome_cliente == '1':
                    return False
                else:
                    if self.__validadores.Validadores.validar_nome(nome_cliente):
                        return nome_cliente
                    else:
                        self.__utilitarios.Utilitarios.mensagem_de_erro(f'O valor "{nome_cliente}" é inválido.')


    def __onter_cpf_cliente(self):
        while True:
            self.__utilitarios.Utilitarios.limpar_terminal()
            self.__interfaces.Interfaces.imprimir_menu('Adicionando Cliente', 'Adicionando Cliente')
            self.__interfaces.Interfaces.imprimir_menu('Informe o CPF do cliente', 'Informe o CPF do cliente', ['Voltar'])
            cpf_cliente = input('| -> ').strip()

            if cpf_cliente == '1':
                return False
            else:
                if self.__validadores.Validadores.validar_cpf(cpf_cliente):
                    return cpf_cliente
                else:
                    self.__utilitarios.Utilitarios.mensagem_de_erro(f'O valor "{cpf_cliente}" é inválido.')


    def __confirmar_cliente(self, nome_cliente, cpf_cliente):
        while True:
            self.__utilitarios.Utilitarios.limpar_terminal()
            self.__interfaces.Interfaces.imprimir_menu(f'Nome: {nome_cliente}', 'Confirmar Cliente')
            self.__interfaces.Interfaces.imprimir_menu(f'Nome: {nome_cliente}', f'Nome: {nome_cliente}')
            self.__interfaces.Interfaces.imprimir_menu_confirmacao(f'Nome: {nome_cliente}', f'CPF: {cpf_cliente}')

            confirmacao = input('| -> ').strip()

            if confirmacao == '1':
                return True
            elif confirmacao == '2':
                return False
            else:
                self.__utilitarios.Utilitarios.mensagem_de_erro(f'O valor "{confirmacao}" é inválido.')


    def __adicionar_cliente(self):
        while True:
            nome_cliente = self.__obter_nome_cliente()

            if nome_cliente:
                while True:
                    cpf_cliente = self.__onter_cpf_cliente()
        
                    if cpf_cliente:
                        while True:
                            if self.__confirmar_cliente(nome_cliente, cpf_cliente):
                                self.__salvar_cliente({'nome':nome_cliente, 'cpf':cpf_cliente})

                                self.__utilitarios.Utilitarios.limpar_terminal()
                                self.__interfaces.Interfaces.imprimir_menu('Cliente criado com sucesso', 'Cliente criado com sucesso')
                                self.__interfaces.Interfaces.imprimir_menu_enter_para_continuar('Cliente criado com sucesso')
                                self.__utilitarios.Utilitarios.enter_para_continuar()

                                break
                            else:
                                break
                    else:
                        break

            else:
                break

    
    def __salvar_cliente(self, cliente):
        self.__dados.Dados.adicionar_cliente(cliente)


    def __adicionar_conta(self):
        print()


    # Sair
    def __opcao_sair(self):
        while True:
            self.__utilitarios.Utilitarios.limpar_terminal()
            self.__interfaces.Interfaces.imprimir_menu_sair()
            opcao_menu_sair = input('| -> ')
        
            if self.__validadores.Validadores.validar_opcao_menu(2, opcao_menu_sair):
                if int(opcao_menu_sair) == 2:
                    break
                
                self.__chamar_opcoes_menu_sair(opcao_menu_sair)
            else:
                self.__utilitarios.Utilitarios.mensagem_de_erro(f'O valor "{opcao_menu_sair}" é inválido.')


    def __chamar_opcoes_menu_sair(self, opcao_menu_sair):
        opcao_menu_sair = int(opcao_menu_sair)

        if opcao_menu_sair == 1:
            self.__utilitarios.Utilitarios.limpar_terminal()
            exit()


m = Main()
m.iniciar()
