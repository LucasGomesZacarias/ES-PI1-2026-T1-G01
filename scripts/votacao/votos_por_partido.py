import conexao_bd

def votos_por_partido():
    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            c.partido,
            COUNT(v.id_votacao) AS total_votos
        FROM votacao v
        JOIN candidatos c
            ON v.numero_candidato = c.numero_candidato
        WHERE v.voto_nulo = FALSE
        GROUP BY c.partido
        ORDER BY total_votos DESC
    """)

    rows = cursor.fetchall()

    print("=== Votos por Partido ===")
    if not rows:
        print("Nenhum voto registrado até o momento.")
    else:
        for row in rows:
            print(f"Partido: {row['partido']:<10}  Votos: {row['total_votos']}")

    cursor.close()
    conexao.close()

    return rows