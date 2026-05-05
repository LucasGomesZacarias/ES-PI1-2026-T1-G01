import os
import time
import conexao_bd
import log_ocorrencias
from votacao import zerezima
from gerenciamento import criptografia
from votacao import votacao_menu_principal

def so_numeros(valor):
    for caractere in valor:
        if caractere not in "0123456789":
            return False
    return True

def tentativa ():
    novatentativa = ""
    while novatentativa not in ("SIM"):
        novatentativa = input("Deseja tentar novamente (Sim/Não)").upper()
        if novatentativa in ("SIM"):
            return validaMesario()
        if novatentativa in ("NAO" or "NÃO"):
            return votacao_menu_principal()
        else:
            print("Apenas Sim ou Nao ")
            time.sleep(4)
            os.system('cls')


def validaMesario ():
    conexao=conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)
    os.system ("cls")

    titulo = input("Título de eleitor: ")
    cpf_prefixo = input("4 primeiros dígitos do CPF: ")
    chave_acesso = input("Chave de acesso: ")

    if not titulo or not cpf_prefixo or not chave_acesso:
        log_ocorrencias.log_abertura()
        print("Todos os campos são obrigatórios. Validação falhou.")
        os.system('cls')
        print('==========================================\n\nVoltando.')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nVoltando..')
        time.sleep(1)
        os.system('cls')
        print('==========================================\n\nVoltando...')
        time.sleep(1)
        os.system('cls')

        return tentativa()

    
    if len(cpf_prefixo) != 4 or not so_numeros(cpf_prefixo):
        log_ocorrencias.log_abertura()
        print("Digitos incoerentes maior ou diferente do esperado. Validação falhou.")
        time.sleep(2)
        return tentativa()
    
    titulo_criptografado = criptografia.criptografia(titulo)

    busca = "SELECT * FROM eleitores WHERE titulo_de_eleitor = %s"
    cursor.execute(busca, (titulo_criptografado,))
    resultado = cursor.fetchone()

    if not resultado:
        log_ocorrencias.log_abertura()
        print("Pessoa não encontrada. Validação falhou.")
        time.sleep(2)
        return tentativa()

    cpf_descriptografado = criptografia.descriptografia(resultado["cpf"], True)

    if cpf_descriptografado[:4] == cpf_prefixo:
        print("CPF conferido com sucesso.")
    else:
        print("Dígitos do CPF não conferem. Validação falhou.")
        time.sleep(2)
        return tentativa()

    chave_armazenada = resultado["chave_de_acesso"]
    chave_criptografada = criptografia.criptografia(chave_acesso)

    if chave_criptografada != chave_armazenada:
        log_ocorrencias.log_abertura()
        print("Chave de acesso inválida. Validação falhou.")
        time.sleep(2)
        return tentativa()

    if resultado["mesario"] == False:
        log_ocorrencias.log_abertura()
        print("Acesso negado: usuário não possui perfil de mesário. Validação falhou.")
        time.sleep(2)
        return tentativa()


    zerezima.zerezima()
    log_ocorrencias.log_abertura()
    os.system("cls")
    print(f" Mesário validado com sucesso! Bem vindo(a), {resultado['nome']}.\n")
    return print(f"Nome: {resultado['nome']}\nTítulo de eleitor: {titulo}\nCPF: {cpf_descriptografado}\nMesário: {'Sim' if resultado['mesario'] else 'Não'}",)
 

