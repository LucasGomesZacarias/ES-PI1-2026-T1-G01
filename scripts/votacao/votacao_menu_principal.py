import os
import time
from votacao import votacao_submenus
from gerenciamento import menus

def votacao_menu_principal():
    opcao=0
    while opcao!=4:
        try:
            opcao=int(input('==========================================\nMenu Votação\n\n1. Abrir votação\n2. Auditoria de votação\n3. Resultados da Votação\n4. Voltar\n\nEscolha uma opção: '))
            match opcao:
                case 1:
                    os.system('clear')
                    valida=0
                    votacao_submenus.abrir_votacao(valida)
                case 2:
                    os.system('clear')
                    votacao_submenus.auditoria_votacao()
                    pass
                case 3:
                    os.system('clear')
                    votacao_submenus.resultados_votacao()
                    pass
                case 4:
                    os.system('clear')
                    menus.menu_principal()
                case _:
                    os.system('clear')
                    print('==========================================\nOpção inválida\nvoltando.')
                    time.sleep(1)
                    os.system('clear')
                    print('==========================================\nOpção inválida\nvoltando..')
                    time.sleep(1)
                    os.system('clear')
                    print('==========================================\nOpção inválida\nvoltando...')
                    time.sleep(1)
                    os.system('clear')
        except ValueError:
            os.system('clear')
            print('==========================================\nUtilize números por favor\nvoltando.')
            time.sleep(1)
            os.system('clear')
            print('==========================================\nUtilize números por favor\nvoltando..')
            time.sleep(1)
            os.system('clear')
            print('==========================================\nUtilize números por favor\nvoltando...')
            time.sleep(1)
            os.system('clear')