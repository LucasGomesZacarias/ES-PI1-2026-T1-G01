import os
import time
import random
from gerenciamento import validacaoDeCpf
from gerenciamento import criptografia
from gerenciamento import validacao_titulo
from gerenciamento import menus
import conexao_bd
import rich

def deletar():
    """Busca um eleitor pelo CPF ou título e realiza sua exclusão do banco de dados.

    Solicita confirmação dupla antes de executar a operação de exclusão.
    Chama a si mesma recursivamente em caso de entradas inválidas ou eleitor não encontrado.

    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    #Conexão BD
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)
    valor = input("Digite o CPF ou ti­tulo de eleitor: ")
    
    valor=criptografia.criptografia(valor)

    busca = "SELECT * FROM eleitores WHERE cpf = %s OR titulo_de_eleitor = %s"
    cursor.execute(busca, (valor, valor))
    resultado = cursor.fetchone()
    if resultado:
        os.system('cls' if os.name == 'nt' else 'clear')

        cpf_descriptografado=criptografia.descriptografia(resultado['cpf'], True)
        te_descriptografado=criptografia.descriptografia(resultado['titulo_de_eleitor'], False)
        print(f"=========Eleitor==========\nNome: {resultado['nome']}\nCPF: {cpf_descriptografado}\nTitulo de eleitor: {te_descriptografado}\nMesario: {'Sim' if resultado['mesario'] else 'Não'}")
        escolha = input (f'\n\nDeseja deletar esse eleitor?\nSim ou Não : ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
        if escolha == 'SIM':
            escolha2 = input (f'\n\nDeseja mesmo deletar esse eleitor? Essa ação não poderá ser desfeita\n\nSim ou Não: ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
            if escolha2 == 'SIM':
                    sql = "DELETE FROM eleitores WHERE id_eleitores = %s"
                    cursor.execute(sql, (resultado['id_eleitores'],))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'==========================================\nEleitor deletado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.menu_gerenciamento()
            else:
                deletar()
        elif escolha == 'NÃO' or escolha == 'NAO':
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nNenhum Eleitor Deletado!\n==========================================")
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
            deletar()
            return  
        else:  #tratamento de erro para qualquer outra coisa sem ser sim ou nao
            os.system('cls' if os.name == 'nt' else 'clear')
            rich.print(f"==========================================\n[red]Erro:[/red] A resposta deve ser apenas sim ou não!\n==========================================")
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
            deletar()
            return  
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        rich.print("==========================================\n[red]Erro:[/red] Eleitor não encontrado\n==========================================")
        time.sleep(2)
        deletar()
