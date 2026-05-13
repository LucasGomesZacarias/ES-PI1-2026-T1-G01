import os
import conexao_bd

def listar_candidatos_alf():

    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print (f"==========================================\nListar Candidatos")

    cursor.execute("SELECT c.nome AS Candidato, c.partido AS Partido, c.numero_candidato AS Numero, COUNT(*) AS Votos FROM candidatos c LEFT JOIN  votacao v ON c.numero_candidato = v.numero_candidato GROUP BY c.numero_candidato ORDER BY c.nome")
    for (nome, partido, numero_candidato, votos) in cursor.fetchall():

        print(f"\n\n---------------------------------\nNome: {nome} \nPartido: {partido} \nNúmero do candidato: {numero_candidato}\nVotos: {votos}")
