import os
import time
import random
import mysql.connector
from gerenciamento import validacaoDeCpf
from gerenciamento import criptografia
from gerenciamento import validacao_titulo
from gerenciamento import menus
import conexao_bd

def editar():
    
    os.system ("cls")
    #Conexão BD
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)
    valor = input("Digite o CPF ou ti­tulo de eleitor: ")
    
    valor=criptografia.criptografia(valor)

    busca = "SELECT * FROM eleitores WHERE cpf = %s OR titulo_de_eleitor = %s"
    cursor.execute(busca, (valor, valor))
    resultado = cursor.fetchone()
    if resultado:
        os.system ("cls")

        cpf_descriptografado=criptografia.descriptografia(resultado['cpf'], True)
        te_descriptografado=criptografia.descriptografia(resultado['titulo_de_eleitor'], False)


        opcao = int(input(f"=========Eleitor==========\nNome: {resultado['nome']}\nCPF: {cpf_descriptografado}\nTitulo de eleitor: {te_descriptografado}\nMesario: {'Sim' if resultado['mesario'] else 'Não'}\n\nQual Opção Deseja Editar:\n1.0 Nome\n2.0 CPF\n3.0 Título Eleitor\n4.0 Mesário\n5.0 Todos\n\nEscolha Sua Opção: "))
        match opcao:
            case 1:
                    nome = input(f"==========================================\nEditar Eleitor\n\nNome: ")
                    if nome is None or nome == "":
                        os.system('cls')
                        print (f"==========================================\nErro: O nome não pode ser vazio\n==========================================")
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
                        editar()
                        return
                    #tratamento de erro para nome incompleto
                    if len(nome.split()) < 2:
                        os.system('cls')
                        print (f"==========================================\nErro: Informe o nome completo!\n==========================================")
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
                        editar()
                        return
                    #tratamento de erro para nome com número
                    for caractere in nome:
                        if caractere in "0123456789":
                            os.system('cls')
                            print (f"==========================================\nErro: O nome não pode conter números\n==========================================")
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
                            editar()
                            return
                    partes_nome = nome.split() #divide o nome para pegar partes dele para criar a nova chave
                    chave_de_acesso = partes_nome[0][:2].upper() + partes_nome[1][0].upper() + str(random.randint(1000, 9999))
                    sql = "UPDATE eleitores SET nome = %s, chave_de_acesso = %s WHERE id = %s"
                    cursor.execute(sql, (nome, chave_de_acesso, resultado['id']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls')
                    print(f'==========================================\nEleitor editado com sucesso!\n\nNova Chave de acesso: {chave_de_acesso}\n\n==========================================')
                    time.sleep(3)
                    os.system('cls')
                    menus.menu_gerenciamento()

            case 2:
                    cpf = (input(f"CPF do Eleitor: "))
                    #tratamento de erro cpf maior ou menor q 11 digitos
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
                        editar()
                        return
                    #tratamento de erro para letras no cpf
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
                        editar()
                        return
                    #validação cpf
                    if not validacaoDeCpf.validaCpf(cpf):
                        os.system('cls')
                        print (f"==========================================\nErro: CPF INVALIDO !\n==========================================")
                        time.sleep(2)
                        editar()
                        return 
                    criptografia_cpf = criptografia.criptografia(cpf)
                    cursor.execute("SELECT * FROM eleitores WHERE cpf = %s AND id != %s", (criptografia_cpf, resultado['id']))
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
                        editar()
                        return
                    sql = "UPDATE eleitores SET cpf = %s WHERE id = %s"
                    cursor.execute(sql, (criptografia_cpf, resultado['id']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls')
                    print(f'==========================================\nEleitor editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls')
                    menus.menu_gerenciamento()

            case 3:
                    titulo_eleitor = input(f"Titulo de Eleitor: ")

                    criptografia_TE = criptografia.criptografia(titulo_eleitor)
                    cursor.execute("SELECT * FROM eleitores WHERE titulo_de_eleitor = %s AND id != %s", (criptografia_TE, resultado['id']))
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
                        editar()
                        return

                    #tratamento de erro titulo maior ou menor q 12 letras
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
                        editar()
                        return
                    #tratamento de erro para titulo com letras
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
                        editar()
                        return
                    #validacao de titulo
                    if not validacao_titulo.validacaoTitulo(titulo_eleitor):
                        os.system('cls')
                        print (f"==========================================\nErro: TÍTULO INVALIDO !\n==========================================")
                        time.sleep(2)
                        editar()
                        return
                    sql = "UPDATE eleitores SET titulo_de_eleitor = %s WHERE id = %s"
                    cursor.execute(sql, (criptografia_TE, resultado['id']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls')
                    print(f'==========================================\nEleitor editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls')
                    menus.menu_gerenciamento()
                    
            case 4:
                    mesario = input (f'Mesário? (Sim ou Não): ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
                    if mesario == 'SIM':
                        mesario =1 #1 é verdadeiro no BD
                    elif mesario == 'NÃO' or mesario == 'NAO':
                        mesario = 0 #2 é falso no BD
                    else:  #tratamento de erro para qualquer outra coisa sem ser sim ou nao
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
                        editar()
                        return
                    sql = "UPDATE eleitores SET mesario = %s WHERE id = %s"
                    cursor.execute(sql, (mesario, resultado['id']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls')
                    print(f'==========================================\nEleitor editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls')
                    menus.menu_gerenciamento()

            case 5:
                    nome = input(f"==========================================\nCadastrar Eleitor\n\nNome: ")
                    if nome is None or nome == "":
                        os.system('cls')
                        print (f"==========================================\nErro: O nome não pode ser vazio\n==========================================")
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
                        editar()
                        return
                    if len(nome.split()) < 2:
                        os.system('cls')
                        print (f"==========================================\nErro: Informe o nome completo!\n==========================================")
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
                        editar()
                        return
                    for caractere in nome:
                        if caractere in "0123456789":
                            os.system('cls')
                            print (f"==========================================\nErro: O nome não pode conter números\n==========================================")
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
                            editar()
                            return
                              
                    titulo_eleitor = input(f"Titulo de Eleitor: ")

                    criptografia_TE = criptografia.criptografia(titulo_eleitor)
                    cursor.execute("SELECT * FROM eleitores WHERE titulo_de_eleitor = %s AND id != %s", (criptografia_TE, resultado['id']))
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
                        editar()
                        return

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
                        editar()
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
                        editar()
                        return
                    if not validacao_titulo.validacaoTitulo(titulo_eleitor):
                        os.system('cls')
                        print (f"==========================================\nErro: TÍTULO INVALIDO !\n==========================================")
                        time.sleep(2)
                        editar()
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
                        editar()
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
                        editar()
                        return
                    if not validacaoDeCpf.validaCpf(cpf):
                        os.system('cls')
                        print (f"==========================================\nErro: CPF INVALIDO !\n==========================================")
                        time.sleep(2)
                        editar()
                        return
                    criptografia_cpf = criptografia.criptografia(cpf)
                    cursor.execute("SELECT * FROM eleitores WHERE cpf = %s AND id != %s", (criptografia_cpf, resultado['id']))
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
                        editar()
                        return

                    #input mesario
                    mesario = input (f'Mesário? (Sim ou Não): ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
                    if mesario == 'SIM':
                        mesario =1 #1 é verdadeiro no BD
                    elif mesario == 'NÃO' or mesario == 'NAO':
                        mesario = 0 #2 é falso no BD
                    else:  #tratamento de erro para qualquer outra coisa sem ser sim ou nao
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
                        editar()
                        return

                    partes_nome = nome.split() #divide o nome para pegar partes dele para criar a chave
                    chave_de_acesso = partes_nome[0][:2].upper() + partes_nome[1][0].upper() + str(random.randint(1000, 9999))
                    #insert no BD
                    sql = "UPDATE eleitores SET nome = %s, cpf = %s, titulo_de_eleitor = %s, mesario = %s, chave_de_acesso = %s WHERE id = %s"
                    cursor.execute(sql, (nome, criptografia_cpf, criptografia_TE, mesario, chave_de_acesso, resultado['id']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls')
                    print(f'==========================================\nEleitor editado com sucesso!\n\nNova Chave de acesso: {chave_de_acesso}\n\n==========================================')
                    time.sleep(3)
                    os.system('cls')
                    menus.menu_gerenciamento()

                    
    else:
        os.system ("cls")
        print("Eleitor não encontrado")
        time.sleep(2)
        editar()
