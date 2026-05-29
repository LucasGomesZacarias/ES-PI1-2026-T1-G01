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

        print(f"=========candidato==========\nNome: {resultado['nome']}\nPartido: {resultado['partido']}\nNúmedo de candidato: {resultado['numero_candidato']}")
        escolha = input (f'\n\nDeseja deletar esse candidato?\nSim ou Não : ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
        if escolha == 'SIM':
            escolha2 = input (f'\n\nDeseja mesmo deletar esse candidato? Essa ação não poderá ser desfeita\n\nSim ou Não: ').upper() #upper pra deixar respostas tudo em maiusculo para o tratamento de erro a seguir
            if escolha2 == 'SIM':
                    sql = "DELETE FROM candidatos WHERE id_candidatos = %s"
                    cursor.execute(sql, (resultado['id_candidatos'],))
                    conexao.commit()
                    cursor.close()
                    conexao.close()
                    #mensagem final 
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'==========================================\ncandidato deletado com sucesso!\n\n==========================================')
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    menus.gerenciamento_candidato()
            else:
                deletar()
        elif escolha == 'NÃO' or escolha == 'NAO':
            os.system('cls' if os.name == 'nt' else 'clear')
            print (f"==========================================\nNenhum candidato Deletado!\n==========================================")
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
        rich.print("==========================================\n[red]Erro:[/red] Candidato não encontrado\n==========================================")
        time.sleep(2)
        deletar()
