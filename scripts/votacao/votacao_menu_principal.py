import os
import time
from votacao import votacao_submenus
from gerenciamento import menus
import rich

def header(): 
    rich.print ("==========================================\n        ELEIÇÕES[blue]PUC[/blue]   |   2026")

def votacao_menu_principal():
    opcao=0
    while opcao!=4:
        try:
            header()
            opcao=int(input('==========================================\n| MENU VOTAÇÃO\n|\n| 1.0 Abrir votação\n| 2.0 Auditoria de votação\n| 3.0 Resultados da Votação\n| 4.0 Voltar\n|------------------------------------------\n| Escolha uma opção: '))
            match opcao:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    valida=0
                    votacao_submenus.abrir_votacao(valida)
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    votacao_submenus.auditoria_votacao()
                    pass
                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    votacao_submenus.resultados_votacao()
                    pass
                case 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.menu_principal()
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