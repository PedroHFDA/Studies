# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# string = 'Pedro' # Str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    pass

p1 = Pessoa()
p1.nome = 'Pedro'
p1.sobrenome = 'Albuquerque'

p2 = Pessoa()
p2.nome = 'Luisa'
p2.sobrenome = 'Carreiro'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)