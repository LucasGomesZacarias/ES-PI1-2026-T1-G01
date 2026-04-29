import random
from scripts.gerenciamento.criptografia import criptografia, descriptografia
import mysql.connector
import datetime

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Augusto0609@',
    database='banco_dados_pi'
)
cursor = conexao.cursor()

def gerar_protocolo(numero_candidato):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letra1 = random.choice(letras)
    letra2 = random.choice(letras)
    if numero_candidato < 10:
        numero_atualizado = "0" + str(numero_candidato)
    else:
        numero_atualizado = str(numero_candidato)
    digitos = ""
    for i in range (5):
        digitos += str(random.randint(0, 9))
    protocolo = "V" + letra1 + letra2 + "26" + numero_atualizado + digitos
    protocolo_criptografado = criptografia(protocolo, None) 
    return protocolo, protocolo_criptografado    

def salvar_protocolo(protocolo_criptografado, numero_candidato, voto_nulo):
    sql = "INSERT INTO votacao (protocolo_votacao, numero_candidato, voto_nulo, dia) VALUES (%s, %s, %s, %s)"
    valores = (protocolo_criptografado, numero_candidato, voto_nulo, datetime.date.today())
    cursor.execute(sql, valores)
    conexao.commit()

def listar_protocolo():
    sql = "SELECT protocolo_votacao FROM votacao"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    protocolos = []
    for linha in resultado:
        protocolo_descriptografado = descriptografia(linha[0], None)
        protocolos.append(protocolo_descriptografado)
    protocolos.sort()
    for protocolo in protocolos:
        print(protocolo)
