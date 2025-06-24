# Escrever uma função que recebe uma lista de strings contendo nomes de pessoas como parâmetro e devolve o nome mais curto, 
# o nome mais curto que tiver dentro dessa lista de strings. A função deve ignorar espaços antes e depois do nome e deve devolver o nome,
# entre aspas, capitalizado, ou seja, apenas com a primeira letra maiúscula.

def mais_curto(lista_de_nomes):
    nomes_tratados = [nome.strip() for nome in lista_de_nomes]
    nome_curto = nomes_tratados[0]

    for nome in nomes_tratados:
        if len(nome) < len(nome_curto):
            nome_curto = nome

    return nome_curto.capitalize()


lista = ['pedro', 'Alberto', 'leo']
print(mais_curto(lista))

