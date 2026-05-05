import os
import time
import conexao_bd
from gerenciamento import criptografia
from votacao import votacao_menu_principal, votacao_submenus
def so_numeros(valor):
    for caractere in valor:
        if caractere not in "0123456789":
            return False
    return True

def tentativa_E():
    novatentativa = ""
    while novatentativa not in ("SIM", "NAO", "NÃO"):
        novatentativa = input("Deseja tentar novamente (Sim/Não)").upper()
        if novatentativa in ("SIM"):
            return encerrarVotacao()
        if novatentativa in ("NAO", "NÃO"):
            valida=1
            votacao_submenus.abrir_votacao(valida)
        else:
            print("Apenas Sim ou Nao ")
            time.sleep(4)
            os.system('clear')
            tentativa_E()



def encerrarVotacao():
    conexao = conexao_bd.conexao_bd()
    cursor = conexao.cursor(dictionary=True)
    os.system("clear")

    titulo = input("Título de eleitor: ")
    cpf_prefixo = input("4 primeiros dígitos do CPF: ")
    chave_acesso = input("Chave de acesso: ")

    if not titulo or not cpf_prefixo or not chave_acesso:
        print("Todos os campos são obrigatórios. Validação falhou.")
        os.system('clear')
        print('==========================================\n\nVoltando.')
        time.sleep(1)
        os.system('clear')
        print('==========================================\n\nVoltando..')
        time.sleep(1)
        os.system('clear')
        print('==========================================\n\nVoltando...')
        time.sleep(1)
        os.system('clear')
        tentativa_E()

    if len(cpf_prefixo) != 4 or not so_numeros(cpf_prefixo):
        print("Digitos incoerentes maior ou diferente do esperado. Validação falhou.")
        time.sleep(2)
        tentativa_E()

    titulo_criptografado = criptografia.criptografia(titulo)

    busca = "SELECT * FROM eleitores WHERE titulo_de_eleitor = %s"
    cursor.execute(busca, (titulo_criptografado,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Pessoa não encontrada. Validação falhou.")
        time.sleep(2)
        tentativa_E()

    cpf_descriptografado = criptografia.descriptografia(resultado["cpf"], True)

    if cpf_descriptografado[:4] == cpf_prefixo:
        print("CPF conferido com sucesso.")
    else:
        print("Dígitos do CPF não conferem. Validação falhou.")
        time.sleep(2)
        tentativa_E()

    chave_armazenada = resultado["chave_de_acesso"]
    chave_criptografada = criptografia.criptografia(chave_acesso)

    if chave_criptografada != chave_armazenada:
        print("Chave de acesso inválida. Validação falhou.")
        time.sleep(2)
        tentativa_E()

    if resultado["mesario"] == False:
        print("Acesso negado: usuário não possui perfil de mesário. Validação falhou.")
        time.sleep(2)
        tentativa_E()

    
    os.system('clear')
    confirmacao = input("Deseja realmente encerrar a votação? (Sim/Não): ").upper()

    
    if confirmacao in ("NÃO", "NAO"):
        os.system('clear')
        print("Encerramento cancelado. Retornando ao menu anterior.")
        time.sleep(2)
        valida=1
        votacao_submenus.abrir_votacao(valida)

    
    if confirmacao==("SIM"):
        os.system('clear')
        segunda_chave = input("Digite novamente sua chave de acesso para confirmar: ")

        
        segunda_chave_criptografada = criptografia.criptografia(segunda_chave)

        if segunda_chave_criptografada != chave_armazenada:
            print("Chave de acesso inválida. Encerramento cancelado.")
            time.sleep(2)
            tentativa_E()

        os.system('clear')
        print(f"Votação encerrada com sucesso! Obrigado(a), {resultado['nome']}.\n") 
        print(f"Nome: {resultado['nome']}\nTítulo de eleitor: {titulo}\nCPF: {cpf_descriptografado}\nMesário: {'Sim' if resultado['mesario'] else 'Não'}")
        time.sleep(5)
        votacao_menu_principal.votacao_menu_principal()

    else:
        print("Resposta inválida. Apenas Sim ou Não são aceitos.")
        time.sleep(2)
        tentativa_E()