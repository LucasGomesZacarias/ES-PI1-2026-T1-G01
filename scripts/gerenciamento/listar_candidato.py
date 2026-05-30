import os
import time
import random 
import conexao_bd

def listar_candidato():
    """Lista todos os candidatos cadastrados no banco de dados.

    Recupera e exibe nome, partido e número de candidato de cada registro.

    Returns:
        None
    """
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print (f"==========================================\nListar Candidato")

    cursor.execute("SELECT nome, partido, numero_candidato FROM candidatos")
    for (nome, partido, numero_candidato) in cursor.fetchall():
        print(f"\n\n---------------------------------\nNome: {nome} \nPartido: {partido} \nNúmedo de candidato: {numero_candidato}")