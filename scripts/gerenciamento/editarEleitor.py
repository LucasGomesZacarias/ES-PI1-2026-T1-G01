import os
import time
import random 

def editar():
    os.system ("cls")
    print (f"==========================================\nEditar Eleitor")

def listar_eleitor():
    os.system ("cls")
    print (f"==========================================\nListar Eleitor")

def cadastrar_eleitor():
    os.system ("cls")

    nome = input(f"==========================================\nCadastrar Eleitor\n\nNome: ")
    
    #tratamento de erro nome 
    if nome == "":
        os.system('cls')
        print (f"==========================================\nErro: o nome não pode ser vazio\n==========================================")
        time.sleep(2)
        os.system('cls')
        print('==========================================\n\nvoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando...')
        time.sleep(1)
        os.system('cls')
        cadastrar_eleitor()
        return
    
    for caractere in nome:
        if caractere in "0123456789":
            os.system('cls')
            print (f"==========================================\nErro: o nome não pode conter números\n==========================================")
            time.sleep(2)
            os.system('cls')
            print('==========================================\n\nvoltando.')
            time.sleep(1)
            os.system('cls')
            print('==========================================\n\nvoltando..')
            time.sleep(1)
            os.system('cls')
            print('==========================================\n\nvoltando...')
            time.sleep(1)
            os.system('cls')
            cadastrar_eleitor()
            return

            

    titulo = input(f"Titulo de Eleitor: ")


    #tratamento de erro titulo
    if len(titulo) != 12:
        os.system('cls')
        print (f"==========================================\nErro: Título deve conter exatos 12 números!\n==========================================")
        time.sleep(2)
        os.system('cls')
        print('==========================================\n\nvoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando...')
        time.sleep(1)
        os.system('cls')
        cadastrar_eleitor()
        return
    
    try:
        int(titulo)
    except ValueError:
        os.system('cls')
        print (f"==========================================\nErro: Título deve conter apenas números!\n==========================================")
        time.sleep(2)
        os.system('cls')
        print('==========================================\n\nvoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando...')
        time.sleep(1)
        os.system('cls')
        cadastrar_eleitor()
        return


    cpf = (input(f"CPF do Eleitor: "))

    if len(cpf) != 11:
        os.system('cls')
        print (f"==========================================\nErro: CPF deve conter exatos 11 números!\n==========================================")
        time.sleep(2)
        os.system('cls')
        print('==========================================\n\nvoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando...')
        time.sleep(1)
        os.system('cls')
        cadastrar_eleitor()
        return
    
    try:
        int(cpf)
    except ValueError:
        os.system('cls')
        print (f"==========================================\nErro: CPF deve conter apenas números!\n==========================================")
        time.sleep(2)
        os.system('cls')
        print('==========================================\n\nvoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando...')
        time.sleep(1)
        os.system('cls')
        cadastrar_eleitor()
        return
    

    mesario = input (f'Mesário? (Sim ou Não): ').upper()
    if mesario == 'SIM':
        mesario =1
    elif mesario == 'NÃO':
        mesario = 0 
    else:
        os.system('cls')
        print (f"==========================================\nErro: A resposta deve ser apenas sim ou não!\n==========================================")
        time.sleep(2)
        os.system('cls')
        print('==========================================\n\nvoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nvoltando...')
        time.sleep(1)
        os.system('cls')
        cadastrar_eleitor()
        return
    


def deletar_eleitor():
    os.system ("cls")
    print (f"==========================================\nDeletar Eleitor")

def buscar_eleitor(conexao):
    os.system ("cls")
    cursor=conexao.cursor()
    valor= input("Digite o CPF ou tÃ­tulo de eleitor: ")
    busca = "SELECT * FROM eleitores WHERE cpf = %s OR titulo_de_eleitor = %s"
    cursor.execute(busca, (valor, valor))
    resultado = cursor.fetchone()
    if resultado:
        print(f"=========Eleitor==========\nID: {resultado['id_eleitores']}\nNome: {resultado['nome']}\nCPF: {resultado['cpf']}\nTitulo de eleitor: {resultado['titulo_de_eleitor']}\nMesario: {resultado['mesario']}\nChave de acesso: {resultado['chave_de_acesso']}\nConfirmaÃ§Ã£o de voto: {resultado['confirmacao_de_voto']}")
    else:
        print("Eleitor não encontrado")