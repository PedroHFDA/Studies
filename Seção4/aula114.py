# Funções recursivas e recursividade 

# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)
#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso recursivo  
#     # Contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)

# print(recursiva(0,998))


def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))