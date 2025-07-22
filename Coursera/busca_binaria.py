def busca(lista,elemento):
    primeiro = 0
    ultimo = len(lista) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        print(meio)

        if lista[meio] == elemento:
            return meio
        
        elif elemento < lista[meio]:
            ultimo = meio - 1

        else:
            primeiro = meio + 1

    return False

def bubble_sort(lista):
    fim = len(lista)

    for i in range(fim-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
    return lista


def insertion_sort(lista):
    for i in range(1, len(lista)):
        analisado = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > analisado:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = analisado
    
    return lista