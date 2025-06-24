
def soma_matrizes(m1, m2):
    if len(m1) != len(m2):
        return False
    
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            return False
        
    resultado = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[i])):
            linha.append(m1[i][j] + m2[i][j])
        resultado.append(linha)

    return resultado