import conexao_bd

def votos_por_partido():
    """Exibe a contagem de votos válidos agrupada por partido político.

    Realiza consulta no banco de dados excluindo votos nulos e agrupa os resultados
    por partido em ordem decrescente de votos.

    Returns:
        list: Lista de dicionários com as chaves 'partido' e 'total_votos'.
    """
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