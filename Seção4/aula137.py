class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
    


class Motor:
    def __init__(self, nome):
        self.nome = nome



class Fabricante:
    def __init__(self, nome):
        self.nome = nome


supra = Carro('Supra')
toyota = Fabricante('Toyota')
motor_3_0 = Motor (3.0)
supra.fabricante = toyota
supra.motor = motor_3_0
print(supra.nome, supra.fabricante.nome, supra.motor.nome)

jesko = Carro('jesko')
koenigsegg = Fabricante('koenigsegg')
motor_v8 = Motor ('V8')
jesko.fabricante = koenigsegg
jesko.motor = motor_v8
print(jesko.nome, jesko.fabricante.nome, jesko.motor.nome)