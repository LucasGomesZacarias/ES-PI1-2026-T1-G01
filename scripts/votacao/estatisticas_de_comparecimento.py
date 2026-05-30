import conexao_bd

def estatisticas_comparecimento():
    """Calcula e exibe estatísticas de comparecimento eleitoral.

    Consulta o banco de dados para obter o total de eleitores cadastrados,
    o total que já votou e o percentual de comparecimento.

    Returns:
        dict: Dicionário com as chaves 'total_eleitores', 'total_votantes'
              e 'percentual_comparecimento'.
    """
    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            COUNT(*)                                    AS total_eleitores,
            SUM(confirmacao_de_voto = TRUE)             AS total_votantes,
            ROUND(
                SUM(confirmacao_de_voto = TRUE) * 100.0
                / COUNT(*), 2
            )                                           AS percentual_comparecimento
        FROM eleitores
    """)

    row = cursor.fetchone()

    print("=== Estatísticas de Comparecimento ===")
    print(f"Total de eleitores cadastrados : {row['total_eleitores']}")
    print(f"Total de eleitores que votaram : {row['total_votantes']}")
    print(f"Percentual de comparecimento   : {row['percentual_comparecimento']}%")

    cursor.close()
    conexao.close()

    return row