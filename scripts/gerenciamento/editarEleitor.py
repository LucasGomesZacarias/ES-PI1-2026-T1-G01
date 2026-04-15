import os
import time


def editar():
    os.system ("cls")
    print (f"==========================================\nEditar Eleitor")

def listar_eleitor():
    os.system ("cls")
    print (f"==========================================\nListar Eleitor")

def cadastrar_eleitor():
    os.system ("cls")
    print (f"==========================================\nCadastrar Eleitor")

def deletar_eleitor():
    os.system ("cls")
    print (f"==========================================\nDeletar Eleitor")

def buscar_eleitor(conexao, valor):
    os.system ("cls")
    cursor=conexao.cursor()
    busca = "SELECT * FROM eleitores WHERE cpf = %s OR titulo_de_eleitor = %s"
    cursor.execute(busca, (valor, valor))
    resultado = cursor.fetchone()
    return resultado