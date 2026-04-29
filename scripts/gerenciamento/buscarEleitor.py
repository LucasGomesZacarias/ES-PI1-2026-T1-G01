import os
import time
import random 
import mysql.connector
from gerenciamento import criptografia

def buscar_eleitor():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='07112cep',
        database='projeto_pi'
    )
    os.system ("cls")
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

        print(f"=========Eleitor==========\nNome: {resultado['nome']}\nCPF: {cpf_descriptografado}\nTitulo de eleitor: {te_descriptografado}\nMesario: {'Sim' if resultado['mesario'] else 'Nao'}\nConfirmação de voto: {resultado['confirmacao_de_voto']}")
    else:
        os.system ("cls")
        print("Eleitor não encontrado")
        time.sleep(2)
        buscar_eleitor()

        