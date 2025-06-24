def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    print(f"{linhas}X{colunas}")