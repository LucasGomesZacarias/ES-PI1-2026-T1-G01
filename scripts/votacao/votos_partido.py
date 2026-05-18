import os
import conexao_bd

def votos_por_partido():
    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"==========================================\nVotos por Partido")

    cursor.execute("""
        SELECT c.partido AS Partido, COUNT(v.id_votacao) AS Votos
        FROM candidatos c
        LEFT JOIN votacao v
               ON v.numero_candidato = c.numero_candidato
              AND v.voto_nulo = FALSE
        GROUP BY c.partido
        ORDER BY Votos DESC
    """)
    partidos = cursor.fetchall()

    if not partidos:
        print("Nenhum dado disponível.")
    else:
        for partido, votos in partidos:
            print(f"\n---------------------------------\nPartido: {partido}\nVotos: {votos}")

            
