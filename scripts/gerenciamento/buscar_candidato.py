import os
import time
import random 
import conexao_bd

def buscar_candidato():
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

        