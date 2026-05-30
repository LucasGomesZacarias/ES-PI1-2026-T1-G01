import random
import conexao_bd
from gerenciamento.criptografia import criptografia, descriptografia
from votacao import protocolo_votacao
import time
from votacao import log_ocorrencias

conexao = conexao_bd.conexao_bd()

def identificar_eleitor(titulo, quatro_digitos_cpf, chave):
    """Busca e valida um eleitor no banco de dados com base nas credenciais fornecidas.

    Args:
        titulo (str): Título de eleitor com 12 dígitos.
        quatro_digitos_cpf (str): Primeiros 4 dígitos do CPF do eleitor.
        chave (str): Chave de acesso do eleitor.

    Returns:
        dict | None: Dicionário com os dados do eleitor se as credenciais forem válidas,
                     ou None se qualquer validação falhar.
    """
    cursor = conexao.cursor(dictionary=True)
    titulo_criptografado = criptografia(titulo)
    cursor.execute("SELECT * FROM eleitores WHERE titulo_de_eleitor = %s", (titulo_criptografado,))
    eleitor = cursor.fetchone()
    cursor.close()

    if eleitor is None:
        return None

    cpf_salvo = eleitor["cpf"]
    cpf_descriptografado = descriptografia(cpf_salvo, True)
    if cpf_descriptografado[:4] != quatro_digitos_cpf:
        return None

    if eleitor["chave_de_acesso"] != criptografia(chave):
        return None

    return eleitor
# Busca o eleitor no banco e valida seus dados (CPF e chave de acesso).

def buscar_candidato(numero):
    """Busca um candidato no banco de dados pelo número informado.

    Args:
        numero (int): Número do candidato a ser buscado.

    Returns:
        dict | None: Dicionário com os dados do candidato se encontrado, ou None caso contrário.
    """
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM candidatos WHERE numero_candidato = %s", (numero,))
    candidato = cursor.fetchone()
    cursor.close()

    return candidato
# Busca um candidato no banco pelo número informado.



def registrar_voto(numero_candidato, voto_nulo):
    """Gera o protocolo e salva o voto no banco de dados.

    Args:
        numero_candidato (str): Número do candidato votado, ou None para voto nulo.
        voto_nulo (bool): True se o voto for nulo, False caso contrário.

    Returns:
        str: Protocolo de votação em texto claro para exibição ao eleitor.
    """
    protocolo, protocolo_criptografado = protocolo_votacao.gerar_protocolo(numero_candidato)
    protocolo_votacao.salvar_protocolo(protocolo_criptografado, numero_candidato, voto_nulo)
    return protocolo
# Registra o voto no banco de dados com protocolo criptografado.

def marcar_como_votou(id_eleitor):
    """Atualiza o campo confirmacao_de_voto do eleitor para TRUE no banco de dados.

    Args:
        id_eleitor (int): Identificador único do eleitor na tabela eleitores.

    Returns:
        None
    """
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE eleitores SET confirmacao_de_voto = TRUE WHERE id_eleitores = %s",
        (id_eleitor,)
    )
    conexao.commit()
    cursor.close()
# Atualiza o status do eleitor para indicar que ele já votou.

def votar():
    """Conduz o fluxo completo de votação de um eleitor.

    Coleta e valida as credenciais do eleitor, verifica se já votou, permite
    escolher o candidato, solicita confirmação e registra o voto com protocolo.

    Returns:
        int | None: Retorna 1 após voto registrado com sucesso, ou None em caso de falha na identificação.
    """
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
        log_ocorrencias.log_duplo()
        print("Este eleitor ja votou.")
    
        return
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
            print("Candidato não encontrado.")
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
    log_ocorrencias.log_voto()
    return 1



