import random
from gerenciamento.criptografia import criptografia, descriptografia
import datetime
import conexao_bd


conexao=conexao_bd.conexao_bd()
cursor = conexao.cursor()


def gerar_protocolo(numero_candidato):
    """Gera um protocolo único de votação e retorna sua versão original e criptografada.

    O protocolo é composto pelo prefixo 'V', duas letras aleatórias, ano '26',
    número do candidato formatado com 2 dígitos e 5 dígitos aleatórios.

    Args:
        numero_candidato (int): Número do candidato votado. Pode ser None para voto nulo.

    Returns:
        tuple: Par (str, str) contendo o protocolo em texto claro e o protocolo criptografado.
    """
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra1 = random.choice(letras)
    letra2 = random.choice(letras)
    numero_candidato=int(numero_candidato)
    if numero_candidato is None:
        numero_atualizado = "00"
        
    
    elif numero_candidato < 10:
        numero_atualizado = "0" + str(numero_candidato)
    else:
        numero_atualizado = str(numero_candidato)
    digitos = ""
    for i in range (5):
        digitos += str(random.randint(0, 9))
    protocolo = "V" + letra1 + letra2 + "26" + numero_atualizado + digitos
    protocolo_criptografado = criptografia(protocolo) 
    print(protocolo_criptografado)
    return protocolo, protocolo_criptografado    

def salvar_protocolo(protocolo_criptografado, numero_candidato, voto_nulo):
    """Salva o protocolo de votação criptografado no banco de dados.

    Args:
        protocolo_criptografado (str): Protocolo de votação já criptografado.
        numero_candidato (str): Número do candidato votado, ou None para voto nulo.
        voto_nulo (bool): True se o voto foi nulo, False caso contrário.

    Returns:
        None
    """
    sql = "INSERT INTO votacao (protocolo_votacao, numero_candidato, voto_nulo, dia) VALUES (%s, %s, %s, %s)"
    valores = (protocolo_criptografado, numero_candidato, voto_nulo, datetime.date.today())
    cursor.execute(sql, valores)
    conexao.commit()

def listar_protocolo():
    """Lista todos os protocolos de votação descriptografados em ordem alfabética.

    Recupera os protocolos do banco, descriptografa cada um e os exibe ordenados.

    Returns:
        None
    """
    sql = "SELECT protocolo_votacao FROM votacao"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    protocolos = []
    for linha in resultado:
        protocolo_descriptografado = descriptografia(linha[0], False)
        protocolos.append(protocolo_descriptografado)
    protocolos.sort()
    for protocolo in protocolos:
        print(protocolo)
