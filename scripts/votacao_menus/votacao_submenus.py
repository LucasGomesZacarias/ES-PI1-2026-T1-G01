import votacao_menu_principal
import os
import time


def abrir_votacao():
    opcao=0
    while opcao!=3:
        try:
            opcao=int(input('==========================================\nMenu Abrir Votação\n\n1. Voto\n2. Encerrar votação\n3. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls')
                    pass
                case 2:
                    #colocar depois a função pra voltar pro menu principal da votação quando encerrar a votação
                    os.system('cls')
                    pass
                case 3:
                    votacao_menu_principal.votacao_menu_principal() #apagar depois a opção voltar, aqui ta só pra teste
                case _:
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('cls')


def auditoria_votacao():
    opcao=0
    while opcao!=3:
        try:
            opcao=int(input('==========================================\nMenu Auditoria da Votação\n\n1. Exibir logs de ocorrências\n2. Exibir protocolos de votação\n3. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls')
                    pass
                case 2:
                    os.system('cls')
                    pass
                case 3:
                    os.system('cls')
                    votacao_menu_principal.votacao_menu_principal()
                case _:
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('cls')


def resultados_votacao():
    opcao=0
    while opcao!=3:
        try:
            opcao=int(input('==========================================\nResultados da votação\n\n1. Boletim de urna\n2. Estatísticas de comparecimento\n3. Votos por partido\n4. Validação de integridade\n5. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls')
                    pass
                case 2:
                    os.system('cls')
                    pass
                case 3:
                    os.system('cls')
                    pass
                case 4:
                    os.system('cls')
                    pass
                case 5:
                    os.system('cls')
                    votacao_menu_principal.votacao_menu_principal()
                case _:
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('cls')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('cls')
        except ValueError:
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('cls')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('cls')