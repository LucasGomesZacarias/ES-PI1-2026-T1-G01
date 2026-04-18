def validaCpf(cpf):
    if len(set(cpf)) == 1:
        return False

    # Primeiro digito verificador 
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    resto = soma % 11

    if resto < 2:
        primeiro_dv = 0
    else:
        primeiro_dv = 11 - resto

    if primeiro_dv >= 10:
        primeiro_dv = 0

    if primeiro_dv != int(cpf[9]):
        return False

    # Segundo digito verificador 
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    resto = soma % 11
    if resto < 2:
        segundo_dv = 0
    else:
        segundo_dv = 11 - resto

    if segundo_dv >= 10:
        segundo_dv = 0

    if segundo_dv != int(cpf[10]):
        return False

    return True