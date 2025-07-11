class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, outro):
        lados1 = sorted([self.a, self.b, self.c])
        lados2 = sorted([outro.a, outro.b, outro.c])

        razao1 = lados1[0] / lados2[0]
        razao2 = lados1[1] / lados2[1]
        razao3 = lados1[2] / lados2[2]

        epsilon = 0.0001

        return (
            abs(razao1 - razao2) < epsilon and
            abs(razao2 - razao3) < epsilon
        )