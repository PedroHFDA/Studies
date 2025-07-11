def menor_nome(nomes):
    menor = None
    for nome in nomes:
        nome_formatado = nome.strip().capitalize()
        if menor is None or len(nome_formatado) < len(menor):
            menor = nome_formatado
    return menor