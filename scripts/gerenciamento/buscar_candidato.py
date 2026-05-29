import os
import time
import random 
import conexao_bd

def buscar_candidato():
    """Busca e exibe os dados de um candidato pelo número de candidato.

    Solicita ao usuário o número do candidato, realiza a busca no banco de dados
    e exibe nome, partido e número. Chama a si mesma recursivamente caso o
    candidato não seja encontrado.

    Returns:
        None
    """
    conexao=conexao_bd.conexao_bd()
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = conexao.cursor(dictionary=True)
    valor = input("Digite o número do candidato: ")
    

    busca = "SELECT * FROM candidatos WHERE numero_candidato=%s"
    cursor.execute(busca, (valor,))
    resultado = cursor.fetchone()
    if resultado:
        os.system('cls' if os.name == 'nt' else 'clear')



        print(f"=========candidato==========\nNome: {resultado['nome']}\nPartido: {resultado['partido']}\nNúmero de candidato: {resultado['numero_candidato']}")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("candidato não encontrado")
        time.sleep(2)
        buscar_candidato()

        