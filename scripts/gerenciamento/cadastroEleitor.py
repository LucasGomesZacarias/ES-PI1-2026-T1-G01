import os
import time
import random
import mysql.connector
from gerenciamento import validacaoDeCpf
from gerenciamento import criptografia
from gerenciamento import validacao_titulo
from gerenciamento import menus

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
    criptografia_cpf = criptografia.criptografia(cpf, None)
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

    criptografia_TE = criptografia.criptografia(None, titulo_eleitor)
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

    partes_nome = nome.split()
    chave_de_acesso = partes_nome[0][:2].upper() + partes_nome[1][0].upper() + str(random.randint(1000, 9999))

    sql = "INSERT INTO eleitores (nome, cpf, titulo_de_eleitor, mesario, chave_de_acesso) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nome, criptografia_cpf, criptografia_TE, mesario, chave_de_acesso))
    conexao.commit()
    cursor.close()
    conexao.close()

    os.system('cls')
    print(f'==========================================\nEleitor cadastrado com sucesso!\n\nChave de acesso: {chave_de_acesso}\n\n==========================================')
    time.sleep(3)
    os.system('cls')
    menus.menu_gerenciamento()
