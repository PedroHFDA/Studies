
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_class(self):
        print('Classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    def falar_nome_class(self):
        print('Classe ALUNO')
        print(self.nome, self.sobrenome, self.__class__.__name__)

p1 = Pessoa('Luciane', 'Rodrigues')
p1.falar_nome_class()
c1 = Cliente('Pedro', 'Albuquerque')
c1.falar_nome_class()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_class()