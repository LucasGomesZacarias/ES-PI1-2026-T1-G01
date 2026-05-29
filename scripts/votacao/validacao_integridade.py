import os 
import conexao_bd

def validacao_integridade():
    """Verifica a integridade dos dados comparando votos na urna com eleitores marcados como votados.

    Compara o total de registros na tabela de votação com o total de eleitores
    cuja confirmação de voto está marcada como TRUE, exibindo se há inconsistências.

    Returns:
        None
    """
    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor()

    os.system('cls' if os.name == 'nt' else 'clear')

    cursor.execute("SELECT COUNT(*) FROM votacao")
    total_votos_urna = cursor.fetchone()[0]
 
    cursor.execute("SELECT COUNT(*) FROM eleitores WHERE confirmacao_de_voto = TRUE")
    total_ja_votou = cursor.fetchone()[0]
 
    print(f"==========================================\nValidação de Integridade\n\nVotos registrados na urna: {total_votos_urna}\nEleitores marcados 'Já Votou': {total_ja_votou}")
 
    if total_votos_urna == total_ja_votou:
        print("\nINTEGRO: Os totais coincidem.\nA eleição foi realizada sem inconsistências.")
    else:
        diferenca = abs(total_votos_urna - total_ja_votou)
        print(f"\nINCONSISTENCIA DETECTADA!\nDiferença encontrada: {diferenca} registro(s).\nVerifique o banco de dados.")
