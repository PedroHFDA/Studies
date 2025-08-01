class Pessoa:
    ano = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_clase(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls,nome):
        return cls(nome,50)


    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anônima',idade)


p1 = Pessoa('Pedro', 23)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(27)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(Pessoa.ano)
Pessoa.metodo_de_clase()