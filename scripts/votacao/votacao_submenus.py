from votacao import votacao_menu_principal, log_ocorrencias, protocolo_votacao
from votacao import autenticacao_mesario
from votacao import encerramento
import os
import time
from votacao import protocolo_votacao, registro_votos
from votacao import boletim_urna

def abrir_votacao(valida):
    if valida == 0:
        valida=autenticacao_mesario.validaMesario()


    opcao=0
    while opcao!=3:
        try:
            opcao=int(input('==========================================\nMenu Abrir Votação\n\n1. Voto\n2. Encerrar votação\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    registro_votos.votar()
                case 2:
                    encerramento.encerrarVotacao()
                    os.system('cls' if os.name == 'nt' else 'clear')
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')


def auditoria_votacao():
    opcao=0
    while opcao!=3:
        try:
            opcao=int(input('==========================================\nMenu Auditoria da Votação\n\n1. Exibir logs de ocorrências\n2. Exibir protocolos de votação\n3. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    log_ocorrencias.exibir_logs()
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    protocolo_votacao.listar_protocolo()
                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    votacao_menu_principal.votacao_menu_principal()
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')


def resultados_votacao():
    opcao=0
    while opcao!=3:
        try:
            opcao=int(input('==========================================\nResultados da votação\n\n1. Boletim de urna\n2. Estatísticas de comparecimento\n3. Votos por partido\n4. Validação de integridade\n5. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    boletim_urna.boletim_urna()
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pass
                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pass
                case 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pass
                case 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    votacao_menu_principal.votacao_menu_principal()
                case _:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')