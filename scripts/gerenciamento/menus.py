import os
from gerenciamento.editarEleitor import editar

# separar submenus e munu principal em arquivos diferentes, para não ficar tão grande e confuso.
def listar_eleitor():
    os.system ("cls")
    print (f"==========================================\nListar Eleitor")

def cadastrar_eleitor():
    os.system ("cls")
    print (f"==========================================\nCadastrar Eleitor")

def deletar_eleitor():
    os.system ("cls")
    print (f"==========================================\nDeletar Eleitor")

def menu_principal():
    os.system ("cls")
    op = int(input(f"==========================================\nMenu\n\n1.0 Gerenciamento\n2.0 Votação\n\nEscolha sua opção:"))
    if op ==1:
        os.system ("cls")
        ger = int(input(f"==========================================\nMenu Gerenciamento\n\n1.0 Gerenciamento de Eleitores\n2.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
        if ger == 1:
            os.system ("cls")
            gerele = int(input(f"==========================================\nMenu Gerenciamento de Eleitores\n\n1.0 Editar Eleitor\n2.0 Listar Eleitores\n3.0 Cadastrar Eleitor\n4.0 Deletar Eleitor\n5.0 Voltar ao Menu Principal\n\nEscolha sua opção:"))
            if gerele == 1:
                editar()
            if gerele == 2:
                listar_eleitor()
            if gerele == 3:
                cadastrar_eleitor()
            if gerele == 4:
                deletar_eleitor()
            if gerele == 5:
                menu_principal()
        elif ger ==2:
            os.system ("cls")
            menu_principal()

menu_principal()
