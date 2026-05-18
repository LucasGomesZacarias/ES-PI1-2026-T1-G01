import os
from gerenciamento import editarEleitor
import time
from votacao import votacao_menu_principal
from gerenciamento import buscarEleitor
from gerenciamento import cadastroEleitor
from gerenciamento import deletarEleitor
from gerenciamento import editarEleitor
from gerenciamento import listarEleitor
from gerenciamento import cadastroCandidato, listar_candidato, deletar_candidato, buscar_candidato, editar_candidato

# separar submenus e munu principal em arquivos diferentes, para não ficar tão grande e confuso.

def menu_principal():
    op = 0 
    os.system('cls' if os.name == 'nt' else 'clear')
    while op !=3:
        try:
            op = int(input(f"==========================================\nMenu\n\n1.0 Gerenciamento\n2.0 Votação\n3.0 Encerrar sistema\n\nEscolha sua opção:"))
            match op:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ger = int(input(f"==========================================\nMenu Gerenciamento\n\n1.0 Gerenciamento de Eleitores\n2.0 Gerenciamento de Candidatos\n3.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
                    match ger:
                        case 1:
                            menu_gerenciamento()
                        case 2:
                            gerenciamento_candidato()
                        case 3:
                            menu_principal()
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
                
                
                case 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    votacao_menu_principal.votacao_menu_principal()

                case 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\n                 Saindo.\n==========================================')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\n                 Saindo..\n==========================================')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\n                 Saindo...\n==========================================')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    exit()


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
            menu_principal()

def menu_gerenciamento():
    os.system('cls' if os.name == 'nt' else 'clear')
    gerele = int(input(f"==========================================\nMenu Gerenciamento de Eleitores\n\n1.0 Editar Eleitor\n2.0 Listar Eleitores\n3.0 Cadastrar Eleitor\n4.0 Deletar Eleitor\n5.0 Buscar Eleitor\n6.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
    match gerele:
        case 1:
            editarEleitor.editar()
        case 2:
            listarEleitor.listar_eleitor()
        case 3:
            cadastroEleitor.cadastrar_eleitor()
        case 4:
            deletarEleitor.deletar()
        case 5:
            buscarEleitor.buscar_eleitor()
        case 6:
            menu_principal()
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



def gerenciamento_candidato():
    os.system('cls' if os.name == 'nt' else 'clear')
    gerele = int(input(f"==========================================\nMenu Gerenciamento de Eleitores\n\n1.0 Editar Candidato\n2.0 Listar Candidato\n3.0 Cadastrar Candidato\n4.0 Deletar Candidato\n5.0 Buscar Candidato\n6.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
    match gerele:
        case 1:
            editar_candidato.editar()
        case 2:
            listar_candidato.listar_candidato()
        case 3:
            cadastroCandidato.cadastrar_candidato()
        case 4:
            deletar_candidato.deletar()
        case 5:
            buscar_candidato.buscar_candidato()
        case 6:
            menu_principal()
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


menu_principal()
