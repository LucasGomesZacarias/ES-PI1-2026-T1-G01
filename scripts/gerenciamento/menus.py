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
from tqdm import tqdm
from colorama import Fore, Back, Style, init
import rich
# separar submenus e munu principal em arquivos diferentes, para não ficar tão grande e confuso.
def header():
    """Exibe o cabeçalho padrão do sistema de eleições no terminal.

    Returns:
        None
    """
    rich.print ("|==========================================\n|        ELEIÇÕES[blue]PUC[/blue]   |   2026")

def menu_principal():
    """Exibe e gerencia o menu principal do sistema de eleições.

    Apresenta as opções de Gerenciamento, Votação e encerramento do sistema.
    Permanece em loop até que o usuário escolha encerrar.

    Returns:
        None
    """
    op = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    while op !=3:
        try:
            header()
            op = int(input(f"|==========================================\n| MENU\n|\n| 1.0 Gerenciamento\n| 2.0 Votação\n| 3.0 Encerrar sistema\n|\n|------------------------------------------\n| Escolha sua opção:"))
            match op:
                case 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    header()
                    ger = int(input(f"|==========================================\n| MENU GERENCIAMENTO\n|\n| 1.0 Gerenciamento de Eleitores\n| 2.0 Gerenciamento de Candidatos\n| 3.0 Voltar ao Menu Principal\n|------------------------------------------\n| Escolha sua opção:"))
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
                    print ('\n\n\n\n\n')
                    for i in tqdm(range(100), desc= 'SAINDO' , bar_format="{l_bar}%s{bar}%s{r_bar}" % (Style.BRIGHT + Fore.BLACK, Fore.RESET)):
                        time.sleep(0.02)
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
    """Exibe e gerencia o submenu de gerenciamento de eleitores.

    Apresenta opções para editar, listar, cadastrar, deletar e buscar eleitores,
    além de retornar ao menu principal.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
    gerele = int(input(f"|==========================================\n| MENU GERENCIAMENTO DE ELEITORES\n|\n| 1.0 Editar Eleitor\n| 2.0 Listar Eleitores\n| 3.0 Cadastrar Eleitor\n| 4.0 Deletar Eleitor\n| 5.0 Buscar Eleitor\n| 6.0 Voltar ao Menu Principal\n|------------------------------------------\n| Escolha sua opção:"))
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
    """Exibe e gerencia o submenu de gerenciamento de candidatos.

    Apresenta opções para editar, listar, cadastrar, deletar e buscar candidatos,
    além de retornar ao menu principal.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    header()
    gerele = int(input(f"|==========================================\n| MENU GERENCIAMENTO DE CANDIDATOS\n|\n| 1.0 Editar Candidato\n| 2.0 Listar Candidato\n| 3.0 Cadastrar Candidato\n| 4.0 Deletar Candidato\n| 5.0 Buscar Candidato\n| 6.0 Voltar ao Menu Principal\n|------------------------------------------\n| Escolha sua opção:"))
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



