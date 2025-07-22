import random

def lista_grande(n):
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 1000))
    return lista

def ordena(lista):
    tamanho_lista = len(lista)

    for i in range(tamanho_lista - 1):
        menor_valor = i

        for j in range(i + 1, tamanho_lista):
            if lista[j] < lista[menor_valor]:
                menor_valor = j

        lista[i], lista[menor_valor] = lista[menor_valor], lista[i]

    return lista