import random
import string
from datetime import datetime
import mysql.connector
import conexao_bd
from gerenciamento import criptografia

conexao = conexao_bd.conexao_bd()

def identificar_eleitor(titulo, quatro_digitos_cpf, chave):
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM eleitores WHERE titulo_de_eleitor = %s", (titulo,))
    eleitor = cursor.fetchone()
    cursor.close()

    if eleitor is None:
        return None

    cpf_salvo = eleitor["cpf"]
    if cpf_salvo[:4] != quatro_digitos_cpf:
        return None

    if eleitor["chave_de_acesso"] != criptografia(chave):
        return None

    return eleitor
# Busca o eleitor no banco e valida seus dados (CPF e chave de acesso).

def buscar_candidato(numero):
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM candidatos WHERE numero_candidato = %s", (numero,))
    candidato = cursor.fetchone()
    cursor.close()

    return candidato
# Busca um candidato no banco pelo número informado.

def gerar_protocolo(numero_candidato):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra1 = random.choice(letras)
    letra2 = random.choice(letras)
    cinco_digitos = str(random.randint(10000, 99999))
    numero_formatado = "0" + str(numero_candidato) if numero_candidato < 10 else str(numero_candidato)

    protocolo = "V" + letra1 + letra2 + "26" + numero_formatado + cinco_digitos
    return protocolo
# Gera um protocolo único de votação com letras e números aleatórios.

def registrar_voto(numero_candidato, protocolo_claro, voto_nulo):
    protocolo_cifrado = criptografia(protocolo_claro)
    hoje = datetime.now().strftime("%Y-%m-%d")

    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO votacao (numero_candidato, protocolo_votacao, dia, voto_nulo) VALUES (%s, %s, %s, %s)",
        (numero_candidato, protocolo_cifrado, hoje, voto_nulo)
    )
    conexao.commit()
    cursor.close()
# Registra o voto no banco de dados com protocolo criptografado.

def marcar_como_votou(id_eleitor):
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE eleitores SET confirmacao_de_voto = TRUE WHERE id_eleitores = %s",
        (id_eleitor,)
    )
    conexao.commit()
    cursor.close()
# Atualiza o status do eleitor para indicar que ele já votou.

def votar():
    print("\n--- Identificacao do Eleitor ---")
    titulo = input("Titulo de eleitor: ")
    quatro_digitos = input("4 primeiros digitos do CPF: ")
    chave = input("Chave de acesso: ")

    eleitor = identificar_eleitor(titulo, quatro_digitos, chave)
# Coleta os dados do eleitor para validação.

    if eleitor is None:
        print("Dados invalidos. Acesso negado.")
        return
# Verifica se os dados estão corretos.

    if eleitor["confirmacao_de_voto"] == True:
        print("Este eleitor ja votou.")
# Impede que o eleitor vote mais de uma vez.
                      
    confirmacao = "N"
    while confirmacao != "S":

        print("\n--- Votacao ---")
        numero_digitado = input("Digite o numero do candidato: ")
    try:
        int(numero_digitado)
    except ValueError:

# Tenta converter o número digitado para inteiro.
# Se não for número, pede novamente.

     numero = int(numero_digitado)
     candidato = buscar_candidato(numero)
    if candidato is not None:
            print("Nome:" + candidato["nome"])
            print("Numero:" + str(candidato["numero_candidato"]))
            print("Partido:" + candidato["partido"])
            voto_nulo = False
# Verifica se o candidato existe no banco.
    else:
     print("Candidato nao encontrado.")
     print("Se confirmar, o voto sera NULO.")
     voto_nulo = True
# Caso o candidato não exista, o voto será considerado nulo.

    confirmacao = input("\nConfirmar voto? (S / N): ").upper()
    if confirmacao != "S":
        print("\nVoto cancelado. Digite o numero novamente.")
# Pergunta ao eleitor se deseja confirmar o voto.

    if voto_nulo == True:
        numero_para_banco = None
        numero_para_protocolo = "00"
# Define os dados que serão salvos (candidato ou nulo).
    else:
        numero_para_banco = candidato["numero_candidato"]
        numero_para_protocolo = str(candidato["numero_candidato"])
    protocolo = gerar_protocolo(numero_para_protocolo)
# Gera o protocolo do voto.

    registrar_voto(numero_para_banco, protocolo, voto_nulo)
    marcar_como_votou(eleitor["id_eleitores"])
# Salva o voto, marca eleitor como votado.

    print("\n==================================================")
    print("                 VOTO CONFIRMADO!")
    print("  Protocolo: " + protocolo)
    print("  Guarde este numero como comprovante.")
    print("==================================================")



