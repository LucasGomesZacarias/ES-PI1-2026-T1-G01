import os
import time
import random 
import conexao_bd
from tqdm import tqdm
from colorama import Fore, Back, Style, init


def zerezima():
    """Executa a zerézima: zera todos os votos e reinicia o estado da eleição.

    Apaga todos os registros da tabela de votação, redefine confirmacao_de_voto
    de todos os eleitores para FALSE e limpa o arquivo de log de ocorrências.
    Exibe os candidatos com zero votos após a operação.

    Returns:
        int: Retorna 1 após a conclusão bem-sucedida da zerézima.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in tqdm(range(100), desc= 'EXECUTANDO ZERÉZIMA' , bar_format="{l_bar}%s{bar}%s{r_bar}" % (Style.BRIGHT + Fore.GREEN, Fore.RESET)):
        time.sleep(0.04)
    os.system('cls' if os.name == 'nt' else 'clear')

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
