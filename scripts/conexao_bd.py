import mysql.connector
# Conexão com o banco
def conexao_bd():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Augusto0609@',
        database='banco_dados_pi'
    )

    return conexao


conexao=conexao_bd()

cursor = conexao.cursor()
# ---------- POST: Inserir um novo candidato ----------
'''def inserir_candidato(nome, partido, numero_candidato):
    sql = "INSERT INTO candidatos (nome, partido, numero_candidato) VALUES (%s, %s, %s)"
    valores = (nome, partido, numero_candidato)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Candidato inserido com ID:", cursor.lastrowid)
# ---------- GET: Buscar todos os candidatos ----------
def listar_candidatos():
    cursor.execute("SELECT id, nome, partido, numero_candidato FROM candidatos")
    for (id, nome, partido, numero_candidato) in cursor.fetchall():
        print(f"ID: {id}, Nome: {nome}, Partido: {partido}, Número do Candidato: {numero_candidato}")
# Exemplo de uso
inserir_candidato("Felipe", "ABCD", 13)
listar_candidatos()
# Fechar conexão
cursor.close()
conexao.close()'''
