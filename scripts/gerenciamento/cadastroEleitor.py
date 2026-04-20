import os
import time
import random
import mysql.connector
import validacaoDeCpf
import criptografia
import validacao_titulo

def cadastrar_eleitor():
    os.system ("cls")

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Augusto0609@',
        database='banco_dados_pi'
    )
    cursor = conexao.cursor()

    nome = input(f"==========================================\nCadastrar Eleitor\n\nNome: ")
    
    
    if nome is None or nome == "":
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

            

    titulo_eleitor = input(f"Titulo de Eleitor: ")


    #tratamento de erro titulo
    if len(titulo_eleitor) != 12:
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
        int(titulo_eleitor)
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
    
    if not validacao_titulo.validacaoTitulo(titulo_eleitor):
        os.system('cls')
        print (f"==========================================\nErro: TÍTULO INVALIDO !\n==========================================")
        time.sleep(2)
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
    
    if not validacaoDeCpf.validaCpf(cpf):
       os.system('cls')
       print (f"==========================================\nErro: CPF INVALIDO !\n==========================================")
       time.sleep(2)
       cadastrar_eleitor()
       return

    # criptografia precisa do cpf e do titulo juntos por isso as duas verificações de duplicado fica aqui
    criptografia_cpf = criptografia.criptografia(cpf, titulo_eleitor)[0]
    cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (criptografia_cpf,))
    if cursor.fetchone():
        os.system('cls')
        print("==========================================\nErro: CPF já cadastrado!\n==========================================")
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

    criptografia_TE = criptografia.criptografia(cpf, titulo_eleitor)[1]
    cursor.execute("SELECT * FROM eleitores WHERE titulo_de_eleitor = %s", (criptografia_TE,))
    if cursor.fetchone():
        os.system('cls')
        print("==========================================\nErro: Título de Eleitor já cadastrado!\n==========================================")
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

