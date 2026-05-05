import os
import time
import random 
import conexao_bd

def zerezima ():
    os.system('clear')
    print('==========================================\n\nExecutando ZERÉZIMA.')
    time.sleep(1)
    os.system('clear')
    print('==========================================\n\nExecutando ZERÉZIMA..')
    time.sleep(1)
    os.system('clear')
    print('==========================================\n\nExecutando ZERÉZIMA...')
    time.sleep(1)
    os.system('clear')

    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("DELETE FROM votacao")
    conexao.commit()

    cursor.execute("UPDATE eleitores SET confirmacao_de_voto = FALSE")
    conexao.commit()

    cursor.execute("SELECT numero_candidato, nome, partido FROM candidatos")
    candidatos = cursor.fetchall()

    with open('log_ocorrencias.txt', 'w'):
        pass

    
    print("ZERÉZIMA CONCLUÍDA - TOTAL DE VOTOS POR CANDIDATO:")
    for candidato in candidatos:
        print(f"Candidato: {candidato['nome']} | Partido: {candidato['partido']} | Número: {candidato['numero_candidato']} | Votos: 0")
    print("==========================================\n")

    time.sleep(3)

    cursor.close()
    conexao.close()

    return 1
