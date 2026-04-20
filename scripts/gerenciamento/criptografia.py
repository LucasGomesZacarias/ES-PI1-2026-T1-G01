
def criptografia(cpf, titulo_eleitor):
    tabela=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']#36
    
    
    matriz_chave=[
                  [2,1],
                  [3,2]
                ]
    

    #Criptograrfia CPF
    if cpf != None:
        cpf=str(cpf)
        
        cpf=cpf+cpf[-1:]#dupllica o último caractere do cpf
        

        
        matriz_cpf=[]
        
        
        for par in range(0, len(cpf), 2): #le cpf do começo formando pares de 2
            par=list(cpf[par:par+2])
            par_indices=[]#auxilia a guardar os valores dos pares na tabela a26
            for num in par:
                posicao=tabela.index(str(num)) # Acha a posição na tabela
                par_indices.append(posicao)  
            matriz_cpf.append(par_indices) 

        


        multiplicacao = [[0] * len(matriz_chave) for vazio in range(len(matriz_cpf))]#cria uma matriz baseada nas outras e zera
        

        for col in range(len(matriz_cpf)):#percorre a matriz do cpf
            for linha in range(len(matriz_chave)):#percorre a matriz chave
                for k in range(len(matriz_chave[0])):#define o tamanho da matriz chave(garante o produto escalar)
                    multiplicacao[col][linha] += matriz_chave[linha][k] * int(matriz_cpf[col][k])#multiplica linha por coluna e somma para todos os valores

        
        
        for col in range(len(multiplicacao)):#perocrre a matriz
            for linha in range(2):#separa os pares
                multiplicacao[col][linha]=multiplicacao[col][linha]%36

        

        texto_cifrado=[]
        for col in range(len(multiplicacao)):
            texto_cifrado.append(multiplicacao[col][0])
            texto_cifrado.append(multiplicacao[col][1])#transforma a matriz em um única lista

        
        criptografia_cpf=''
        for num in texto_cifrado:
            criptografia_cpf+=str(tabela[num])#adiciona todos os caracteres em uma única string
        return criptografia_cpf
    else:



        #Criptografia título de eleitor
        if titulo_eleitor != None:
            titulo_eleitor=str(titulo_eleitor)

            titulo_eleitor_matriz=[]

            for par in range(0, len(titulo_eleitor), 2): #le cpf do começo formando pares de 2
                par=list(titulo_eleitor[par:par+2])
                par_indices=[]#auxilia a guardar os valores dos pares na tabela a26
                for num in par:
                    posicao=tabela.index(str(num)) # Acha a posição na tabela
                    par_indices.append(posicao) 
                titulo_eleitor_matriz.append(par_indices) 

            


            multiplicacao = [[0] * len(matriz_chave) for _ in range(len(titulo_eleitor_matriz))]#cria uma matriz baseada nas outras e zera
            

            for col in range(len(titulo_eleitor_matriz)):#percorre a matriz do cpf
                for linha in range(len(matriz_chave)):#percorre a matriz chave
                    for k in range(len(matriz_chave[0])):#define o tamanho da matriz chave(garante o produto escalar)
                        multiplicacao[col][linha] += matriz_chave[linha][k] * int(titulo_eleitor_matriz[col][k])#multiplica linha por coluna e somma para todos os valores

            
            for col in range(len(multiplicacao)):
                for linha in range(2):
                    multiplicacao[col][linha]=multiplicacao[col][linha]%36

            

            texto_cifrado=[]
            for col in range(len(multiplicacao)):#percorre toda a matriz e adiciona tudo em uma lista única
                texto_cifrado.append(multiplicacao[col][0])
                texto_cifrado.append(multiplicacao[col][1])
            
            criptografia_titulo_eleitor=''
            for num in texto_cifrado:
                criptografia_titulo_eleitor+=str(tabela[num])


            return criptografia_titulo_eleitor
        else:
            return criptografia_cpf, criptografia_titulo_eleitor




def descriptografia(cpf, titulo_eleitor):
    tabela=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']#36
    
    
    matriz_chave=[
                  [2,-1],
                  [-3,2]
                ]
    

    #Descriptograrfia CPF

    cpf=str(cpf)


    
    matriz_cpf=[]
    
    
    for par in range(0, len(cpf), 2): #le titilo de eleitor do começo formando pares de 2
        par=list(cpf[par:par+2])
        par_indices=[]#auxilia a guardar os valores dos pares na tabela a26
        for letra in par:
            posicao=tabela.index(str(letra)) # Acha a posição na tabela
            par_indices.append(posicao) 
        matriz_cpf.append(par_indices) 



    multiplicacao = [[0] * len(matriz_chave) for _ in range(len(matriz_cpf))]#cria uma matriz baseada nas outras e zera

    for col in range(len(matriz_cpf)):#percorre a matriz do titulo de eleitor
        for linha in range(len(matriz_chave)):#percorre a matriz chave
            for k in range(len(matriz_chave[0])):#define o tamanho da matriz chave(garante o produto escalar)
                multiplicacao[col][linha] += matriz_chave[linha][k] * int(matriz_cpf[col][k])#multiplica linha por coluna e somma para todos os valores

    
    for col in range(len(multiplicacao)):
        for linha in range(2):
            multiplicacao[col][linha]=multiplicacao[col][linha]%36

    

    texto_cifrado=[]
    for col in range(len(multiplicacao)):
        texto_cifrado.append(multiplicacao[col][0])
        texto_cifrado.append(multiplicacao[col][1])
    
    descriptografia_cpf=''
    for num in texto_cifrado:
        descriptografia_cpf+=str(tabela[num])
    
    descriptografia_cpf=descriptografia_cpf[:-1]



    #Descriptografia título de eleitor

    titulo_eleitor=str(titulo_eleitor)

    titulo_eleitor_matriz=[]

    for par in range(0, len(titulo_eleitor), 2): #le cpf do começo formando pares de 2
        par=list(titulo_eleitor[par:par+2])
        par_indices=[]#auxilia a guardar os valores dos pares na tabela a26
        for letra in par:
            posicao=tabela.index(str(letra)) # Acha a posição na tabela
            par_indices.append(posicao)
        titulo_eleitor_matriz.append(par_indices) 



    multiplicacao = [[0] * len(matriz_chave) for vazio in range(len(titulo_eleitor_matriz))]#cria uma matriz baseada nas outras e zera
    

    for col in range(len(titulo_eleitor_matriz)):#percorre a matriz do cpf
        for linha in range(len(matriz_chave)):#percorre a matriz chave
            for k in range(len(matriz_chave[0])):#define o tamanho da matriz chave(garante o produto escalar)
                multiplicacao[col][linha] += matriz_chave[linha][k] * int(titulo_eleitor_matriz[col][k])#multiplica linha por coluna e somma para todos os valores

    
    
    for col in range(len(multiplicacao)):
        for linha in range(2):
            multiplicacao[col][linha]=multiplicacao[col][linha]%36

    

    texto_cifrado=[]
    for col in range(len(multiplicacao)):
        texto_cifrado.append(multiplicacao[col][0])
        texto_cifrado.append(multiplicacao[col][1])
    
    descriptografia_titulo_eleitor=''
    for num in texto_cifrado:
        descriptografia_titulo_eleitor+=str(tabela[num])


    return descriptografia_cpf, descriptografia_titulo_eleitor



'''cpf=input('digite cpf: ')
titulo_eleitor=input('digite titlo eleitor: ')

criptografia_cpf=criptografia(cpf, titulo_eleitor)[0]#sempre puxar assim nos outros arquivos [0]=cpf [1]=tiutlo de eleitor
criptografia_TE=criptografia(cpf, titulo_eleitor)[1]

descriptografia_cpf=descriptografia(criptografia_cpf, criptografia_TE)[0]
descriptografia_TE=descriptografia(criptografia_cpf, criptografia_TE)[1]

print(criptografia_cpf, descriptografia_cpf, criptografia_TE, descriptografia_TE)'''