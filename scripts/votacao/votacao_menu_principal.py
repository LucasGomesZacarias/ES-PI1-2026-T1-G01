import os
import time
from votacao import votacao_submenus

def votacao_menu_principal():
    opcao=0
    while opcao!=4:
        try:
            opcao=int(input('==========================================\nMenu Votação\n\n1. Abrir votação\n2. Auditoria de votação\n3. Resultados da Votação\n4. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls')
                    votacao_submenus.abrir_votacao()
                case 2:
                    os.system('cls')
                    votacao_submenus.auditoria_votacao()
                    pass
                case 3:
                    os.system('cls')
                    votacao_submenus.resultados_votacao()
                    pass
                case 4:
                    os.system('cls')
                    pass
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