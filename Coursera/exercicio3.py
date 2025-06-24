def imprime_matriz(matriz):
    for linha in matriz:
        for i in range(len(linha)):
            if i == len(linha) - 1:
                print(linha[i])
            else:
                print(linha[i], end=' ')