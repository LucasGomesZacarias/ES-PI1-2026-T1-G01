import os
import conexao_bd

def boletim_urna():

    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print (f"==========================================\nCandidatos")

    cursor.execute("SELECT c.nome AS Candidato, c.partido AS Partido, c.numero_candidato AS Numero, COUNT(v.numero_candidato) AS Votos FROM candidatos c LEFT JOIN  votacao v ON c.numero_candidato = v.numero_candidato GROUP BY c.numero_candidato ORDER BY c.nome")
    for (nome, partido, numero_candidato, votos) in cursor.fetchall():

        print(f"\n\n---------------------------------\nNome: {nome} \nPartido: {partido} \nNúmero do candidato: {numero_candidato}\nVotos: {votos}")
    cursor.execute("SELECT c.nome AS Candidato, c.partido AS Partido, c.numero_candidato AS Numero, COUNT(v.numero_candidato) AS Votos FROM candidatos c LEFT JOIN  votacao v ON c.numero_candidato = v.numero_candidato GROUP BY c.numero_candidato ORDER BY Votos DESC LIMIT 1")
    vencedor = cursor.fetchone()
    if vencedor:
        nome, partido, numero_candidato, votos = vencedor
        print(f"\n---------------Resultado da eleiçcão---------------\nVENCEDOR\n\nNome: {nome} \nPartido: {partido} \nNúmero do candidato: {numero_candidato}\nVotos: {votos}")
    else: 
        print("Nenhum voto registrado")