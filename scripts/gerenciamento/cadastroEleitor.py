import os
import time
import random
from gerenciamento import validacaoDeCpf
from gerenciamento import criptografia
from gerenciamento import validacao_titulo
from gerenciamento import menus
import conexao_bd

def cadastrar_eleitor(nome=None, titulo_eleitor=None, cpf=None, mesario=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    #Conexão BD
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    #input nome
    if nome is None:
        nome = input(f"==========================================\nCadastrar Eleitor\n\nNome: ")
        #COLOCAR TRATAMENTO PARA NOME INCOMPLETO, É NECESSARIO ESCREVER PELO MENOS O PRIMEIRO E SEGUNDO NOME
        #tratamento de erro para nome vázio
        if nome is None or nome == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: O nome não pode ser vazio\n==========================================")
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
            cadastrar_eleitor()
            return
        #tratamento de erro para nome incompleto
        if len(nome.split()) < 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: Informe o nome completo!\n==========================================")
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
            cadastrar_eleitor()
            return
        #tratamento de erro para nome com número
        for caractere in nome:
            if caractere in "0123456789":
                os.system('cls' if os.name == 'nt' else 'clear')
                print (f"==========================================\nErro: O nome não pode conter números\n==========================================")
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
                cadastrar_eleitor()
                return

    #input título
    if titulo_eleitor is None:
        titulo_eleitor = input(f"Titulo de Eleitor: ")

        #tratamento de erro titulo maior ou menor q 12 letras
        if len(titulo_eleitor) != 12:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: Título deve conter exatos 12 números!\n==========================================")
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
            cadastrar_eleitor(nome=nome)
            return
        #tratamento de erro para titulo com letras
        try:
            int(titulo_eleitor)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: Título deve conter apenas números!\n==========================================")
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
            cadastrar_eleitor(nome=nome)
            return
        #validacao de titulo
        if not validacao_titulo.validacaoTitulo(titulo_eleitor):
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: TÍTULO INVALIDO !\n==========================================")
            time.sleep(2)
            cadastrar_eleitor(nome=nome)
            return

        criptografia_TE = criptografia.criptografia(titulo_eleitor)
        cursor.execute("SELECT * FROM eleitores WHERE titulo_de_eleitor = %s", (criptografia_TE,))
        if cursor.fetchone():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("==========================================\nErro: Título de Eleitor já cadastrado!\n==========================================")
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
            cadastrar_eleitor(nome=nome)
            return
    else:
        criptografia_TE = criptografia.criptografia(titulo_eleitor)

    #input cpf
    if cpf is None:
        cpf = (input(f"CPF do Eleitor: "))
        #tratamento de erro cpf maior ou menor q 11 digitos
        if len(cpf) != 11:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: CPF deve conter exatos 11 números!\n==========================================")
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
            cadastrar_eleitor(nome=nome, titulo_eleitor=titulo_eleitor)
            return
        #tratamento de erro para letras no cpf
        try:
            int(cpf)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: CPF deve conter apenas números!\n==========================================")
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
            cadastrar_eleitor(nome=nome, titulo_eleitor=titulo_eleitor)
            return
        #validação cpf
        if not validacaoDeCpf.validaCpf(cpf):
           os.system('cls' if os.name == 'nt' else 'clear')
           print (f"==========================================\nErro: CPF INVALIDO !\n==========================================")
           time.sleep(2)
           cadastrar_eleitor(nome=nome, titulo_eleitor=titulo_eleitor)
           return

        # criptografia precisa do cpf e do titulo juntos por isso as duas verificações de duplicado fica aqui
        criptografia_cpf = criptografia.criptografia(cpf)
        cursor.execute("SELECT * FROM eleitores WHERE cpf = %s", (criptografia_cpf,))
        if cursor.fetchone():
            os.system('cls' if os.name == 'nt' else 'clear')
            print("==========================================\nErro: CPF já cadastrado!\n==========================================")
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
            cadastrar_eleitor(nome=nome, titulo_eleitor=titulo_eleitor)
            return
    else:
        criptografia_cpf = criptografia.criptografia(cpf)

    #input mesario
    if mesario is None:
        mesario = input (f'Mesário? (Sim ou Não): ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
        if mesario == 'SIM':
            mesario =1 #1 é verdadeiro no BD
        elif mesario == 'NÃO' or mesario == 'NAO':
            mesario = 0 #2 é falso no BD
        else:  #tratamento de erro para qualquer outra coisa sem ser sim ou nao
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nErro: A resposta deve ser apenas sim ou não!\n==========================================")
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
            cadastrar_eleitor(nome=nome, titulo_eleitor=titulo_eleitor, cpf=cpf)
            return

    partes_nome = nome.split() #divide o nome para pegar partes dele para criar a chave
    chave_de_acesso = partes_nome[0][:2].upper() + partes_nome[1][0].upper() + str(random.randint(1000, 9999))
    chave_de_acesso_criptografada=criptografia.criptografia(chave_de_acesso)
    #insert no BD
    sql = "INSERT INTO eleitores (nome, cpf, titulo_de_eleitor, mesario, chave_de_acesso) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nome, criptografia_cpf, criptografia_TE, mesario, chave_de_acesso_criptografada))
    conexao.commit()
    cursor.close()
    conexao.close()
    #mensagem final 
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'==========================================\nEleitor cadastrado com sucesso!\n\nChave de acesso: {chave_de_acesso}\n\n==========================================')
    enter = input('Pressione Enter para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')
    menus.menu_gerenciamento()