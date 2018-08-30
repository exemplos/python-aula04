class Pessoa:
    
    def __init__(self, n, i):
        self.nome = n
        self.idade = i

    def imprimir(self):
        print("{} tem {} anos".format(self.nome, self.idade))    