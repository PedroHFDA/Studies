import json
CAMINHO_ARQUIVO = 'Seção4\\aula127.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('Pedro', 23)
p2 = Pessoa('Luciane', 52)
p3 = Pessoa('Luísa', 22)
bd = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()