def maiusculas(lista):
    letras_m = None
    for frase in lista:
        if ord(frase) >= 65 and ord(frase) <= 90:
            letras_m = frase
    return letras_m