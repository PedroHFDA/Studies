def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def busca(lista, elemento):
    posicao = None
    for i in range(len(lista)):
        if lista[i] == elemento:
            posicao = i
            return posicao
    return False