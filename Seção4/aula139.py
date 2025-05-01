# class MinhaString(str):
#     def upper(self):
#         print('Chamou UPPER')
#         return super().upper()

# string = MinhaString('Pedro')
# print(string.upper())

class A:
    atributo_a = 'Valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'Valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlei o sistema')

    def metodo(self):
        super().metodo() #B
        super(B, self).metodo() #A
        super(A, self).metodo() #?
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())

c = C('atributo', 'Qualquer')
print(c.atributo, c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()