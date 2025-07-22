def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
    
def encontra_impares(lista):
    if len(lista) == 0:
        return []
    
    elif lista[0] % 2 != 0:
        return [lista[0]] + encontra_impares(lista[1:])
    
    else:
        return encontra_impares(lista[1:])
    
def incomodam(n):
    if not isinstance(n, int) or n <= 0:
        return ''
    
    if n == 1:
        return 'incomodam '
    
    else:
        return 'incomodam ' + incomodam(n - 1)
    
def elefantes(n):
    if not isinstance(n, int) or n < 2:
        return ""
    
    if n == 2:
        return "Um elefante incomoda muita gente\n" + \
               f"2 elefantes {incomodam(2)}muito mais\n" + \
               "2 elefantes incomodam muita gente\n"
    
    else:
        return elefantes(n - 1) + \
               f"{n} elefantes {incomodam(n)}muito mais\n" + \
               f"{n} elefantes incomodam muita gente\n"