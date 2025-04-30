class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero) 

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Pedro')
cliente1.inserir_endereco('Sudoeste', 501)
cliente1.inserir_endereco('Lago Sul', 17 )

cliente1.listar_enderecos()