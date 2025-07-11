def primeiro_lex(lista):
    menor = None
    for nome in lista:
        if menor is None or nome < menor:
            menor = nome
    return menor