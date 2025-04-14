#__dict__ e vars

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Pedro', 'idade': 23}

p1 = Pessoa(**dados)
print(p1.__dict__)
print(vars(p1))
print(p1.nome)