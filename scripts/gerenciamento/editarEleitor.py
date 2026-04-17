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
    nome = input(f"==========================================\nCadastrar Eleitor\n\nNome: ")
    titulo = input(f"Titulo de Eleitor: ")
    cpf = int(input(f"CFP do Eleitor: "))
    mesario = input (f'Mesário? (Sim ou Não): ').upper()
    if mesario == 'SIM':
        mesario =1
    else:
        mesario = 0 
    


def deletar_eleitor():
    os.system ("cls")
    print (f"==========================================\nDeletar Eleitor")

def buscar_eleitor(conexao):
    os.system ("cls")
    cursor=conexao.cursor()
    valor= input("Digite o CPF ou tÃ­tulo de eleitor: ")
    busca = "SELECT * FROM eleitores WHERE cpf = %s OR titulo_de_eleitor = %s"
    cursor.execute(busca, (valor, valor))
    resultado = cursor.fetchone()
    if resultado:
        print(f"=========Eleitor==========\nID: {resultado['id_eleitores']}\nNome: {resultado['nome']}\nCPF: {resultado['cpf']}\nTitulo de eleitor: {resultado['titulo_de_eleitor']}\nMesario: {resultado['mesario']}\nChave de acesso: {resultado['chave_de_acesso']}\nConfirmaÃ§Ã£o de voto: {resultado['confirmacao_de_voto']}")
    else:
        print("Eleitor não encontrado")