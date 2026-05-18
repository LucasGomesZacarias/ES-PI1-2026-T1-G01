import os
import conexao_bd

def estatistica_comparecimento():
    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')

    cursor.execute("SELECT COUNT(*) FROM eleitores")
    total_eleitores = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE confirmacao_de_voto = TRUE")
    total_votaram = cursor.fetchone()[0]

    percentual = (total_votaram / total_eleitores * 100) if total_eleitores > 0 else 0

    print(f"==========================================\nEstatística de Comparecimento\n\nTotal de eleitores aptos: {total_eleitores}\nTotal que votaram: {total_votaram}\nPercentual de participação: {percentual:.2f}%")