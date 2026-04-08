import os
from gerenciamento import editarEleitor
import time
from votacao import votacao_menu_principal
# separar submenus e munu principal em arquivos diferentes, para não ficar tão grande e confuso.

def menu_principal():
    os.system ("cls")
    while rodar==0:
        try:
            op = int(input(f"==========================================\nMenu\n\n1.0 Gerenciamento\n2.0 Votação\n\nEscolha sua opção:"))
            match op:
                case 1:
                    os.system ("cls")
                    ger = int(input(f"==========================================\nMenu Gerenciamento\n\n1.0 Gerenciamento de Eleitores\n2.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
                    match ger:
                        case 1:
                            menu_gerenciamento()
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
                
                
                case 2:
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
            menu_principal()

def menu_gerenciamento():
    os.system ("cls")
    gerele = int(input(f"==========================================\nMenu Gerenciamento de Eleitores\n\n1.0 Editar Eleitor\n2.0 Listar Eleitores\n3.0 Cadastrar Eleitor\n4.0 Deletar Eleitor\n5.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
    match gerele:
        case 1:
            editarEleitor.editar()
        case 2:
            editarEleitor.listar_eleitor()
        case 3:
            editarEleitor.cadastrar_eleitor()
        case 4:
            editarEleitor.deletar_eleitor()
        case 5:
            menu_principal()
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

rodar=0

menu_principal()
