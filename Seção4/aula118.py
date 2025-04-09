def adiciona_clientes(nome, lista=None  ):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []
cliente1 = adiciona_clientes('Luisa',lista1)
adiciona_clientes('Pedro', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Luciane')
adiciona_clientes('Lucinda', cliente2)
print(cliente2)
#usa a mesma lista sempre