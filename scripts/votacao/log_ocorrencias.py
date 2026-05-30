from datetime import datetime
def registrar_logs(mensagem):
    """Registra uma mensagem com timestamp no arquivo de log de ocorrências.

    Args:
        mensagem (str): Texto descritivo da ocorrência a ser registrada.

    Returns:
        None
    """
    log_data = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log = log_data + " " + mensagem
    with open ("log_ocorrencias.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(log + "\n")

def log_abertura():
    """Registra no log a abertura oficial da sessão de votação.

    Returns:
        None
    """
    registrar_logs("ABERTURA: Votação iniciada com sucesso. Total de votos zerado")

def log_acesso_negado():
    """Registra no log uma tentativa de acesso negado ao sistema.

    Returns:
        None
    """
    registrar_logs("ALERTA: Tentativa de acesso negado")

def log_duplo():
    """Registra no log uma tentativa de voto duplicado por um eleitor.

    Returns:
        None
    """
    registrar_logs("ALERTA: Tentativa de voto duplo")

def log_voto():
    """Registra no log a realização bem-sucedida de um voto.

    Returns:
        None
    """
    registrar_logs("SUCESSO: Voto realizado com sucesso")

def log_encerramento():
    """Registra no log o encerramento oficial da sessão de votação.

    Returns:
        None
    """
    registrar_logs("ENCERRAMENTO: Votação finalizada com sucesso")

def exibir_logs():
    """Lê e exibe no terminal todos os registros do arquivo de log de ocorrências.

    Returns:
        None
    """
    with open ("log_ocorrencias.txt", "r", encoding="utf-8") as arquivo:
            print(f"==========Lista de logs==========\n")
            for linha in arquivo:
                print(linha)