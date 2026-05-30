import os
import time
import conexao_bd
from votacao import zerezima, log_ocorrencias
from gerenciamento import criptografia
from votacao import votacao_menu_principal

def so_numeros(valor):
    """Verifica se uma string contém apenas dígitos numéricos.

    Args:
        valor (str): String a ser verificada.

    Returns:
        bool: True se todos os caracteres forem dígitos, False caso contrário.
    """
    for caractere in valor:
        if caractere not in "0123456789":
            return False
    return True

def tentativa():
    """Pergunta ao usuário se deseja tentar a autenticação novamente.

    Em caso afirmativo, chama validaMesario(). Em caso negativo, retorna ao
    menu de votação. Chama a si mesma em caso de resposta inválida.

    Returns:
        None
    """
    novatentativa = ""
    while novatentativa not in ("SIM", "NAO", "NÃO"):
        novatentativa = input("Deseja tentar novamente (Sim/Não)").upper()
        if novatentativa in ("SIM"):
            validaMesario()
        elif novatentativa in ("NAO", "NÃO"):
           votacao_menu_principal.votacao_menu_principal()
        else:
            print("Apenas Sim ou Nao ")
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
            tentativa()


def validaMesario():
    """Autentica um mesário verificando título, prefixo do CPF e chave de acesso.

    Consulta o banco de dados para validar as credenciais fornecidas, verifica se
    o eleitor possui perfil de mesário e, em caso de sucesso, executa a zerézima
    e registra a abertura no log.

    Returns:
        None
    """
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)
    os.system('cls' if os.name == 'nt' else 'clear')

    titulo = input("Título de eleitor: ")
    cpf_prefixo = input("4 primeiros dígitos do CPF: ")
    chave_acesso = input("Chave de acesso: ")

    if not titulo or not cpf_prefixo or not chave_acesso:
        log_ocorrencias.log_acesso_negado()
        print("Todos os campos são obrigatórios. Validação falhou.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        tentativa()
        return

    
    if len(cpf_prefixo) != 4 or not so_numeros(cpf_prefixo):
        log_ocorrencias.log_acesso_negado()
        print("Digitos incoerentes maior ou diferente do esperado. Validação falhou.")
        time.sleep(2)
        tentativa()
        return
    
    titulo_criptografado = criptografia.criptografia(titulo)

    busca = "SELECT * FROM eleitores WHERE titulo_de_eleitor = %s"
    cursor.execute(busca, (titulo_criptografado,))
    resultado = cursor.fetchone()
    if not resultado:
        log_ocorrencias.log_acesso_negado()
        print("Pessoa não encontrada. Validação falhou.")
        time.sleep(2)
        tentativa()
        return

    cpf_descriptografado = criptografia.descriptografia(resultado["cpf"], True)

    if cpf_descriptografado[:4] == cpf_prefixo:
        print("CPF conferido com sucesso.")
    else:
        print("Dígitos do CPF não conferem. Validação falhou.")
        log_ocorrencias.log_acesso_negado()
        time.sleep(2)
        tentativa()
        return

    chave_armazenada = resultado["chave_de_acesso"]
    chave_criptografada = criptografia.criptografia(chave_acesso)
    if chave_criptografada != chave_armazenada:
        log_ocorrencias.log_acesso_negado()
        print("Chave de acesso inválida. Validação falhou.")
        time.sleep(2)
        tentativa()
        return

    if resultado["mesario"] == False:
        log_ocorrencias.log_acesso_negado()
        print("Acesso negado: usuário não possui perfil de mesário. Validação falhou.")
        time.sleep(2)
        tentativa()
        return


    zerezima.zerezima()
    log_ocorrencias.log_abertura()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" Mesário validado com sucesso! Bem vindo(a), {resultado['nome']}.\n")
    return print(f"Nome: {resultado['nome']}\nTítulo de eleitor: {titulo}\nCPF: {cpf_descriptografado}\nMesário: {'Sim' if resultado['mesario'] else 'Não'}",)
 

