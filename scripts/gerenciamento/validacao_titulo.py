def validacaoTitulo(titulo):
    if len(titulo) != 12:
        return False
    else:
        digitos_validos = '0123456789'
        titulo_valido = True
    if titulo[0] not in digitos_validos:
        titulo_valido = False
    elif titulo[1] not in digitos_validos:
        titulo_valido = False
    elif titulo[2] not in digitos_validos:
        titulo_valido = False
    elif titulo[3] not in digitos_validos:
        titulo_valido = False
    elif titulo[4] not in digitos_validos:
        titulo_valido = False
    elif titulo[5] not in digitos_validos:
        titulo_valido = False
    elif titulo[6] not in digitos_validos:
        titulo_valido = False
    elif titulo[7] not in digitos_validos:
        titulo_valido = False
    elif titulo[8] not in digitos_validos:
        titulo_valido = False
    elif titulo[9] not in digitos_validos:
        titulo_valido = False
    elif titulo[10] not in digitos_validos:
        titulo_valido = False
    elif titulo[11] not in digitos_validos:
        titulo_valido = False
    # Verifica se o título tem exatamente 12 dígitos e verifica se todos os caracteres são todos números.
        
    if titulo_valido == False:
        return False
    else: 
        numero_sequencial = titulo[0:8] 
        numero_unidade_federativa = titulo[8:10]
        primeiro_digito_verificador_informado = titulo[10]
        segundo_digito_verificador_informado = titulo[11]

        unidade_federativa = int(numero_unidade_federativa)
    # Separa as partes do título de eleitor. 

    if unidade_federativa < 1 or unidade_federativa > 28:
        return False
    else:
        soma_primeiro_digito_verificador = (int(numero_sequencial[0]) * 2 +
                                            int(numero_sequencial[1]) * 3 +
                                            int(numero_sequencial[2]) * 4 +
                                            int(numero_sequencial[3]) * 5 +
                                            int(numero_sequencial[4]) * 6 +
                                            int(numero_sequencial[5]) * 7 +
                                            int(numero_sequencial[6]) * 8 +
                                            int(numero_sequencial[7]) * 9)
        resto_primeiro_digito_verificador = soma_primeiro_digito_verificador % 11
    # Cálculo do primeiro dígito verificador.
    # Múltiplica cada dígito do sequencial por 2,3,4,5,6,7,8,9
    # Logo em seguida, divide a somatória por 11, que o resto é igual ao primeiro dígito verificador.

    if resto_primeiro_digito_verificador == 10:
        primeiro_digito_verificador_calculado = 0
    elif resto_primeiro_digito_verificador == 0 and (unidade_federativa == 1 or unidade_federativa == 2):
        primeiro_digito_verificador_calculado = 1
    else:
        primeiro_digito_verificador_calculado = resto_primeiro_digito_verificador
    # Verifica se o resto for igual a 10, automaticamente o Digito Verificador será 0.
    # Se o Dígito Verificador for igual a 0, e a Unidade Federativa for igual a 1 ou 2, ele vira 1.

    soma_segundo_digito_verificador = (int(numero_unidade_federativa[0])* 7 +
                                    int(numero_unidade_federativa[1]) * 8 +
                                    primeiro_digito_verificador_calculado * 9)
    resto_segundo_digito_verificador = soma_segundo_digito_verificador % 11
    # Cálculo do segundo dígito verificador.
    # Multiplica os dois dígitos da Unidade Federativa e o primeiro Digito Verificador por 7,8 e 9.
    # Logo em seguida, divide a somatória por 11, e o resto é o segundo Digito Verificador. 

    if resto_segundo_digito_verificador == 10:
        segundo_digito_verificador_calculado = 0
    elif resto_segundo_digito_verificador == 0 and (unidade_federativa == 1 or unidade_federativa == 2):
        segundo_digito_verificador_calculado = 1
    else:
        segundo_digito_verificador_calculado = resto_segundo_digito_verificador
    # Mesmo caso do primeiro. 

    if primeiro_digito_verificador_calculado == int(primeiro_digito_verificador_informado) and segundo_digito_verificador_calculado == int(segundo_digito_verificador_informado):
        return True
    else:
        return False
        