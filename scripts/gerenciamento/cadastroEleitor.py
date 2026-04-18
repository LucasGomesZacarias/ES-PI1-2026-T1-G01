import os
import time
import random 
import validacaoDeCpf
import criptografia


def cadastrar_eleitor():
    os.system ("cls")

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

    criptografia_cpf=criptografia.criptografia(cpf, titulo_eleitor)[0]#sempre puxar assim nos outros arquivos [0]=cpf [1]=tiutlo de eleitor
    criptografia_TE=criptografia.criptografia(cpf, titulo_eleitor)[1]

    descriptografia_cpf=criptografia.descriptografia(criptografia_cpf, criptografia_TE)[0]
    descriptografia_TE=criptografia.descriptografia(criptografia_cpf, criptografia_TE)[1]