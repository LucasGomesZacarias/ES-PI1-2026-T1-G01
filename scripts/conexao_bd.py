import mysql.connector
# Conexão com o banco
conexao = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='nome_do_banco'
)
cursor = conexao.cursor()
# ---------- POST: Inserir um novo usuário ----------
def inserir_usuario(nome, cpf):
    sql = "INSERT INTO eleitores (nome, cpf) VALUES (%s, %s)"  #definir para inserir o resto da colunas depois
    valores = (nome, cpf)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário inserido com ID:", cursor.lastrowid)
# ---------- GET: Buscar todos os usuários ----------
def listar_usuarios():
    cursor.execute("SELECT id, nome, email FROM usuarios")
    for (id, nome, cpf) in cursor.fetchall():
        print(f"ID: {id}, Nome: {nome}, Email: {cpf}")
# Exemplo de uso
inserir_usuario("Felipe", "12345678901")
listar_usuarios()
# Fechar conexão
cursor.close()
conexao.close()
