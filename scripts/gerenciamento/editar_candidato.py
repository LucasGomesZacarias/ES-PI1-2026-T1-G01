import os
import time
import random
from gerenciamento import menus
import conexao_bd

def editar():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    #Conexão BD
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)
    valor = input("Digite o número do candidato: ")
    
    busca = "SELECT * FROM candidatos WHERE numero_candidato = %s"
    cursor.execute(busca, (valor,))
    resultado = cursor.fetchone()
    if resultado:
        os.system('cls' if os.name == 'nt' else 'clear')

        opcao = int(input(f"=========Candidato==========\nNome: {resultado['nome']}\nPartido: {resultado['partido']}\nNúmero do candidato: {resultado['numero_candidato']}\n\nQual Opção Deseja Editar:\n1.0 Nome\n2.0 Partido\n3.0 Número do Candidato\n4.0 Todos\n\nEscolha Sua Opção: "))
        match opcao:
            case 1:
                    nome = input(f"==========================================\nEditar Candidato\n\nNome: ")
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
                        editar()
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
                        editar()
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
                            editar()
                            return
                    sql = "UPDATE candidatos SET nome = %s WHERE id_candidatos = %s"
                    cursor.execute(sql, (nome, resultado['id_candidatos']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'==========================================\nCandidato editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.menu_gerenciamento()

            case 2:
                    partido = input(f"==========================================\nEditar Candidato\n\nPartido: ")
                    if partido is None or partido == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print (f"==========================================\nErro: O partido não pode ser vazio\n==========================================")
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
                        editar()
                        return
                    for caractere in partido:
                        if caractere in "0123456789":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print (f"==========================================\nErro: O partido não pode conter números\n==========================================")
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
                            editar()
                            return
                    sql = "UPDATE candidatos SET partido = %s WHERE id_candidatos = %s"
                    cursor.execute(sql, (partido, resultado['id_candidatos']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'==========================================\nCandidato editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.menu_gerenciamento()

            case 3:
                    numero_candidato = input(f"==========================================\nEditar Candidato\n\nNúmero do Candidato: ")
                    if numero_candidato is None or numero_candidato == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print (f"==========================================\nErro: O número não pode ser vazio\n==========================================")
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
                        editar()
                        return
                    try:
                        int(numero_candidato)
                    except ValueError:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print (f"==========================================\nErro: Número de candidato deve conter apenas números!\n==========================================")
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
                        editar()
                        return
                    cursor.execute("SELECT * FROM candidatos WHERE numero_candidato = %s AND id_candidatos != %s", (numero_candidato, resultado['id_candidatos']))
                    if cursor.fetchone():
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("==========================================\nErro: Número de candidato já cadastrado!\n==========================================")
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
                        editar()
                        return
                    sql = "UPDATE candidatos SET numero_candidato = %s WHERE id_candidatos = %s"
                    cursor.execute(sql, (numero_candidato, resultado['id_candidatos']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'==========================================\nCandidato editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.menu_gerenciamento()
                    
            case 4:
                    nome = input(f"==========================================\nEditar Candidato\n\nNome: ")
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
                        editar()
                        return
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
                        editar()
                        return
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
                            editar()
                            return
                          
                    partido = input(f"Partido: ")
                    if partido is None or partido == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print (f"==========================================\nErro: O partido não pode ser vazio\n==========================================")
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
                        editar()
                        return
                    for caractere in partido:
                        if caractere in "0123456789":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print (f"==========================================\nErro: O partido não pode conter números\n==========================================")
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
                            editar()
                            return

                    numero_candidato = input(f"Número do Candidato: ")
                    if numero_candidato is None or numero_candidato == "":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print (f"==========================================\nErro: O número não pode ser vazio\n==========================================")
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
                        editar()
                        return
                    try:
                        int(numero_candidato)
                    except ValueError:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print (f"==========================================\nErro: Número de candidato deve conter apenas números!\n==========================================")
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
                        editar()
                        return
                    cursor.execute("SELECT * FROM candidatos WHERE numero_candidato = %s AND id_candidatos != %s", (numero_candidato, resultado['id_candidatos']))
                    if cursor.fetchone():
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("==========================================\nErro: Número de candidato já cadastrado!\n==========================================")
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
                        editar()
                        return

                    #update no BD
                    sql = "UPDATE candidatos SET nome = %s, partido = %s, numero_candidato = %s WHERE id_candidatos = %s"
                    cursor.execute(sql, (nome, partido, numero_candidato, resultado['id_candidatos']))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'==========================================\nCandidato editado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.menu_gerenciamento()

                    
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Candidato não encontrado")
        time.sleep(2)
        editar()