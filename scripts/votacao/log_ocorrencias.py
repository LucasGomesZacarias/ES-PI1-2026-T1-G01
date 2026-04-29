from datetime import datetime
def registrar_logs(mensagem):
    log_data = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log = log_data + " " + mensagem
    with open ("log_ocorrencias.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(log + "\n")

def log_abertura():
    registrar_logs("ABERTURA: Votação iniciada com sucesso. Total de votos zerado")

def log_acesso_negado():
    registrar_logs("ALERTA: Tentativa de acesso negado")

def log_duplo():
    registrar_logs("ALERTA: Tentativa de voto duplo")

def log_voto():
    registrar_logs("SUCESSO: Voto realizado com sucesso")

def log_encerramento():
    registrar_logs("ENCERRAMENTO: Votação finalizada com sucesso")