
def criptografia(texto):
    tabela=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']#36
    
    
    matriz_chave=[
                  [2,1],
                  [3,2]
                ]
    
    texto=str(texto)

    if len(texto)%2!=0:
        texto=texto+texto[-1]#pega o último caractere e duplica
    
    matriz_texto=[]
    

    for par in range(0, len(texto), 2): #le cpf do começo formando pares de 2
        par=list(texto[par:par+2])
        par_indices=[]#auxilia a guardar os valores dos pares na tabela a26
        for num in par:
            posicao=tabela.index(str(num)) # Acha a posição na tabela
            par_indices.append(posicao)  
        matriz_texto.append(par_indices) 



    multiplicacao = [[0] * len(matriz_chave) for vazio in range(len(matriz_texto))]#cria uma matriz baseada nas outras e zera
    

    for col in range(len(matriz_texto)):#percorre a matriz do cpf
        for linha in range(len(matriz_chave)):#percorre a matriz chave
            for k in range(len(matriz_chave[0])):#define o tamanho da matriz chave(garante o produto escalar)
                multiplicacao[col][linha] += matriz_chave[linha][k] * int(matriz_texto[col][k])#multiplica linha por coluna e somma para todos os valores

    
    
    for col in range(len(multiplicacao)):#perocrre a matriz
        for linha in range(2):#separa os pares
            multiplicacao[col][linha]=multiplicacao[col][linha]%36

    

    texto_cifrado=[]
    for col in range(len(multiplicacao)):
        texto_cifrado.append(multiplicacao[col][0])
        texto_cifrado.append(multiplicacao[col][1])#transforma a matriz em um única lista

    
    criptografia=''
    for num in texto_cifrado:
        criptografia+=str(tabela[num])#adiciona todos os caracteres em uma única string

    return criptografia




def descriptografia(texto, impar):
    tabela=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']#36
    
    
    matriz_chave=[
                  [2,-1],
                  [-3,2]
                ]
    


    texto=str(texto)


    
    matriz_texto=[]
    
    
    for par in range(0, len(texto), 2): #le titilo de eleitor do começo formando pares de 2
        par=list(texto[par:par+2])
        par_indices=[]#auxilia a guardar os valores dos pares na tabela a26
        for letra in par:
            posicao=tabela.index(str(letra)) # Acha a posição na tabela
            par_indices.append(posicao) 
        matriz_texto.append(par_indices) 



    multiplicacao = [[0] * len(matriz_chave) for _ in range(len(matriz_texto))]#cria uma matriz baseada nas outras e zera

    for col in range(len(matriz_texto)):#percorre a matriz do titulo de eleitor
        for linha in range(len(matriz_chave)):#percorre a matriz chave
            for k in range(len(matriz_chave[0])):#define o tamanho da matriz chave(garante o produto escalar)
                multiplicacao[col][linha] += matriz_chave[linha][k] * int(matriz_texto[col][k])#multiplica linha por coluna e somma para todos os valores

    
    for col in range(len(multiplicacao)):
        for linha in range(2):
            multiplicacao[col][linha]=multiplicacao[col][linha]%36

    

    texto_cifrado=[]
    for col in range(len(multiplicacao)):
        texto_cifrado.append(multiplicacao[col][0])
        texto_cifrado.append(multiplicacao[col][1])
    
    descriptografia=''
    for num in texto_cifrado:
        descriptografia+=str(tabela[num])
    
    if impar==True:
        descriptografia=descriptografia[:-1]

    return descriptografia




'''cpf=input('digite cpf: ')
TE=input('digite titulo de eleitor: ')

cpf_criptografado=criptografia(cpf)
cpf_descriptografado=descriptografia(cpf_criptografado, True)

TE_criptografado=criptografia(TE)
TE_descriptografado=descriptografia(TE_criptografado, False)


print(cpf_criptografado, cpf_descriptografado, TE_criptografado, TE_descriptografado)'''

