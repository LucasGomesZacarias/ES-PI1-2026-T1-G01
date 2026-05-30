import os
import time
import random
from gerenciamento import validacaoDeCpf
from gerenciamento import criptografia
from gerenciamento import validacao_titulo
from gerenciamento import menus
import conexao_bd
import rich
def header():
    """Exibe o cabeçalho padrão do sistema de eleições no terminal.

    Returns:
        None
    """
    rich.print ("==========================================\n        ELEIÇÕES[blue]PUC[/blue]   |   2026")

def cadastrar_candidato(nome=None, partido=None, numero_candidato=None):
    """Realiza o cadastro de um novo candidato no banco de dados.

    Solicita interativamente nome, partido e número do candidato com validações.
    Usa recursividade para reexibir o formulário mantendo os campos já validados
    em caso de erro.

    Args:
        nome (str): Nome completo do candidato. Se None, solicita ao usuário.
        partido (str): Nome do partido do candidato. Se None, solicita ao usuário.
        numero_candidato (str): Número do candidato (2 dígitos, entre 10 e 99).
                                Se None, solicita ao usuário.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    #Conexão BD
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    #input nome
    if nome is None:
        header()
        nome = input(f"==========================================\nCadastrar Candidato\n\nNome: ")
        #COLOCAR TRATAMENTO PARA NOME INCOMPLETO, É NECESSARIO ESCREVER PELO MENOS O PRIMEIRO E SEGUNDO NOME
        #tratamento de erro para nome vázio
        if nome is None or nome == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            rich.print (f"==========================================\n[red]Erro:[/red] O nome não pode ser vazio\n==========================================")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastrar_candidato()
            return
        #tratamento de erro para nome incompleto
        if len(nome.split()) < 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            rich.print (f"==========================================\n[red]Erro:[/red] Informe o nome completo!\n==========================================")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastrar_candidato()
            return
        #tratamento de erro para nome com número
        for caractere in nome:
            if caractere in "0123456789":
                os.system('cls' if os.name == 'nt' else 'clear')
                rich.print (f"==========================================\n[red]Erro:[/red] O nome não pode conter números\n==========================================")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando.')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando..')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando...')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                cadastrar_candidato()
                return



    if partido is None:
        header()
        partido = input(f"==========================================\nCadastrar Candidato\n\nPartido: ")
        if partido is None or partido == "":
                os.system('cls' if os.name == 'nt' else 'clear')
                rich.print (f"==========================================\n[red]Erro:[/red] O partido não pode ser vazio\n==========================================")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando.')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando..')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando...')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                cadastrar_candidato(nome=nome)
                return

        for caractere in partido:
                if caractere in "0123456789":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    rich.print (f"==========================================\n[red]Erro:[/red] O nome não pode conter números\n==========================================")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\n\nvoltando.')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\n\nvoltando..')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('==========================================\n\nvoltando...')
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cadastrar_candidato(nome=nome)
                    return





    if numero_candidato is None:
        header()
        numero_candidato = input(f"==========================================\nCadastrar Candidato\n\nNúmero de candidato: ")
        if numero_candidato is None or numero_candidato == "":
                os.system('cls' if os.name == 'nt' else 'clear')
                rich.print (f"==========================================\n[red]Erro:[/red] O número não pode ser vazio\n==========================================")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando.')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando..')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando...')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                cadastrar_candidato(nome=nome, partido=partido)
                return
        try:
            int(numero_candidato)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            rich.print (f"==========================================\n[red]Erro:[/red] Número de candidato deve conter apenas números!\n==========================================")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastrar_candidato(nome=nome, partido=partido)
            return
        if int(numero_candidato)<10 or int(numero_candidato)>=100:
                os.system('cls' if os.name == 'nt' else 'clear')
                rich.print (f"==========================================\n[red]Erro:[/red] O número deve conter 2 dígitos e ser maior que 10\n==========================================")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando.')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando..')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('==========================================\n\nvoltando...')
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                cadastrar_candidato(nome=nome, partido=partido)
                return
        cursor.execute("SELECT * FROM candidatos WHERE numero_candidato = %s", (numero_candidato,))
        if cursor.fetchone():
            os.system('cls' if os.name == 'nt' else 'clear')
            rich.print("==========================================\n[red]Erro:[/red] Número de candidato ja existe!\n==========================================")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando.')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando..')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('==========================================\n\nvoltando...')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastrar_candidato(nome=nome, partido=partido)
            return
   




    


    #insert no BD
    sql = "INSERT INTO Candidatos (nome, partido, numero_candidato) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, partido, numero_candidato))
    conexao.commit()
    cursor.close()
    conexao.close()
    #mensagem final 
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'==========================================\nCandidato cadastrado com sucesso!\n\n==========================================')
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    menus.gerenciamento_candidato()
