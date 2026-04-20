import os
import time
import random 
import mysql.connector
from gerenciamento import criptografia

def buscar_eleitor(conexao):
    os.system ("cls")
    cursor=conexao.cursor()
    valor= input("Digite o CPF ou ti­tulo de eleitor: ")
    busca = "SELECT * FROM eleitores WHERE cpf = %s OR titulo_de_eleitor = %s"
    cursor.execute(busca, (valor, valor))
    resultado = cursor.fetchone()
    if resultado:
        print(f"=========Eleitor==========\nID: {resultado['id_eleitores']}\nNome: {resultado['nome']}\nCPF: {resultado['cpf']}\nTitulo de eleitor: {resultado['titulo_de_eleitor']}\nMesario: {resultado['mesario']}\nChave de acesso: {resultado['chave_de_acesso']}\nConfirmaÃ§Ã£o de voto: {resultado['confirmacao_de_voto']}")
    else:
        print("Eleitor não encontrado")