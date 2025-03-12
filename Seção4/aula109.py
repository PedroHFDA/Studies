# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iterator(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Ana', 'Luiz', 'Leticia',
]
camisetas = [
    ['Preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
    
]

# print_iterator(combinations(pessoas,2))
# print_iterator(permutations(pessoas,2))
print_iterator(product(*camisetas))