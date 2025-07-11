def conta_letras(frase, contar='vogais'):
    vogais = 'AEIOUaeiou'
    formatada = frase.replace(' ','').capitalize()
    contador = 0
    if contar == 'vogais':
        for letra in formatada:
            if letra in vogais:
                contador += 1
    else:
        for letra in formatada:
            if letra not in vogais:
                contador += 1
    return contador
