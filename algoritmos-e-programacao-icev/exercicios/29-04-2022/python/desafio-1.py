"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Icev (https://somosicev.com)

PT-BR:
Desenvolva um programa para ser usado na eleição para
presidente do Centro Acadêmico de Engenharia de Software do
iCEV. O programa deve permitir que os alunos votem nos
candidatos de acordo com os números apresentados na tabela
abaixo. Caso o aluno queira votar nulo, ele deve informar o
número 98. Por outro lado, se ele quiser votar em branco, deve
informar o número 99.
Ao final da votação, o programa deve exibir:
• o total de votos para cada candidato;
• o total de votos nulos;
• o total de votos em branco;
• a porcentagem de votos nulos sobre o
total de votos; e
• a porcentagem de votos em branco
sobre o total de votos.
Para finalizar a votação, o mesário tem que informar o valor
99999 e, para números inválidos de candidato, o programa
deverá mostrar uma mensagem.

Número candidato
10 - João
20 - Maria
30 - Francisco
40 - Raimunda
"""

numero_joao = 10
numero_maria = 20
numero_francisco = 30
numero_raimunda = 40
numero_nulo = 98
numero_branco = 99
numero_sair = 99999

votos_candidato_joao = 0
votos_candidato_maria = 0
votos_candidato_francisco = 0
votos_candidato_raimunda = 0
votos_nulo = 0
votos_branco = 0
quantidade_total_votos = 0

porcentagem_joao =  0
porcentagem_maria = 0
porcentagem_francisco = 0
porcentagem_raimunda = 0
porcentagem_nulo = 0
porcentagem_branco = 0

contador_voto = 1
while True:
    print(f"{'=' * 15} Tabela candidatos {'=' * 15}",
    f"\n[ {numero_joao} ] João",
    f"\n[ {numero_maria} ] Maria",
    f"\n[ {numero_francisco} ] Francisco",
    f"\n[ {numero_raimunda} ] Raimunda",
    f"\n[ {numero_nulo} ] Nulo",
    f"\n[ {numero_branco} ] Branco",
    "\n",
    f"\n[ {numero_sair} ] Sair")

    voto_usuario = input(f"\n[ / ] {contador_voto}º voto\n[ ? ] Digite o número da opção\n[ > ] ").strip()

    verificador_voto_valido = True
    if voto_usuario != str(numero_sair):
        if voto_usuario == str(numero_joao):
            opcao_de_voto_escolhida = "João"

        elif voto_usuario == str(numero_maria):
            opcao_de_voto_escolhida = "Maria"
    
        elif voto_usuario == str(numero_francisco):
            opcao_de_voto_escolhida = "Francisco"
        
        elif voto_usuario == str(numero_raimunda):
            opcao_de_voto_escolhida = "Raimunda"

        elif voto_usuario == str(numero_nulo):
            opcao_de_voto_escolhida = "Nulo"
        
        elif voto_usuario == str(numero_branco):
            opcao_de_voto_escolhida = "Branco"
        
        else:
            verificador_voto_valido = False
            print("\n[ ! ] Valor inserido inválido, tente novamente.")

    else:
        if quantidade_total_votos > 0:
            porcentagem_joao =  votos_candidato_joao / quantidade_total_votos
            porcentagem_maria = votos_candidato_maria / quantidade_total_votos
            porcentagem_francisco = votos_candidato_francisco / quantidade_total_votos
            porcentagem_raimunda = votos_candidato_raimunda / quantidade_total_votos
            porcentagem_nulo = votos_nulo / quantidade_total_votos
            porcentagem_branco = votos_branco / quantidade_total_votos

        break
    
    if verificador_voto_valido:
        while True:
            confirmacao_voto = input(f"\n[ ? ] Confirmação de voto\n[ / ] Opção | {opcao_de_voto_escolhida}\n[ / ] Número | {voto_usuario}\n\n[ S ] Para confirmar\n[ N ] Para recusar\n[ > ] ").strip().upper()
            
            if confirmacao_voto == "S":
                voto_validado = True

            elif confirmacao_voto == "N":
                voto_validado = False
                print("\n[ / ] Voto cancelado")
                break

            else:
                voto_validado = False
                print("\n[ ! ] Valor inserido inválido, tente novamente.")
            
            if voto_validado:
                print("\n[ / ] Voto validado\n")
                break
    
        if voto_validado:
            quantidade_total_votos += 1

            if voto_usuario == str(numero_joao):
                votos_candidato_joao += 1

            elif voto_usuario == str(numero_maria):
                votos_candidato_maria += 1
        
            elif voto_usuario == str(numero_francisco):
                votos_candidato_francisco += 1
            
            elif voto_usuario == str(numero_raimunda):
                votos_candidato_raimunda += 1

            elif voto_usuario == str(numero_nulo):
                votos_nulo += 1
            
            else:
                votos_branco += 1
                
        contador_voto += 1

print(f"\n[ {votos_candidato_joao} ] | [ {porcentagem_joao:.2%} ] | João",
f"\n[ {votos_candidato_maria} ] | [ {porcentagem_maria:.2%} ] | Maria",
f"\n[ {votos_candidato_francisco} ] | [ {porcentagem_francisco:.2%} ] | Francisco",
f"\n[ {votos_candidato_raimunda} ] | [ {porcentagem_raimunda:.2%} ] | Raimunda",
f"\n[ {votos_nulo} ] | [ {porcentagem_nulo:.2%} ] | Nulo",
f"\n[ {votos_branco} ] | [ {porcentagem_branco:.2%} ] | Branco",)
