import random
from datetime import datetime
import conexao_bd
from gerenciamento import criptografia
from votacao import protocolo_votacao
import time

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
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM candidatos WHERE numero_candidato = %s", (numero,))
    candidato = cursor.fetchone()
    cursor.close()

    return candidato
# Busca um candidato no banco pelo número informado.



def registrar_voto(numero_candidato, voto_nulo):
    protocolo_votacao.gerar_protocolo(numero_candidato)
    hoje = datetime.now().strftime("%Y-%m-%d")

    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO votacao (numero_candidato, protocolo_votacao, dia, voto_nulo) VALUES (%s, %s, %s, %s)",
        (numero_candidato, hoje, voto_nulo)
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
    print(titulo)
    quatro_digitos = input("4 primeiros digitos do CPF: ")
    print(quatro_digitos)
    chave = input("Chave de acesso: ")
    print(chave)

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
        try:
            numero= int(input("Digite o numero do candidato: "))
    
        except ValueError:
            print("Digite apenas números")
            time.sleep(5)
            continue

    # Tenta converter o número digitado para inteiro.
    # Se não for número, pede novamente.

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
# Define os dados que serão salvos (candidato ou nulo).
    else:
        numero_para_banco = str(candidato["numero_candidato"])
# Gera o protocolo do voto.

    protocolo=registrar_voto(numero_para_banco, voto_nulo)
    marcar_como_votou(eleitor["id_eleitores"])
# Salva o voto, marca eleitor como votado.

    print("\n==================================================")
    print("                 VOTO CONFIRMADO!")
    print("  Protocolo: " + protocolo)
    print("  Guarde este numero como comprovante.")
    print("==================================================")

    return 1



