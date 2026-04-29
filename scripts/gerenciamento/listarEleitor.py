import os
import time
import random 
import conexao_bd
from gerenciamento import criptografia


def listar_eleitor():

    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system ("cls")
    print (f"==========================================\nListar Eleitor")

    cursor.execute("SELECT nome, cpf, titulo_de_eleitor, mesario, confirmacao_de_voto FROM eleitores")
    for (nome, cpf, titulo_de_eleitor, mesario, confirmacao_de_voto) in cursor.fetchall():
        cpf=criptografia.descriptografia(cpf, True)
        titulo_de_eleitor=criptografia.descriptografia(titulo_de_eleitor, False)
        
        if mesario==1:
            mesario='Sim'
        else:
            mesario='Não'

        print(f"\n\n---------------------------------\nNome: {nome} \nCPF: {cpf} \nTítulo de eleitor: {titulo_de_eleitor} \nMesário: {mesario} \nConfirmação de voto: {confirmacao_de_voto}")
