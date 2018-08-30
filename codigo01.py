

class Aluno:
    pass

a = Aluno()
b = Aluno()

a.nome = 'Maria'
b.nome = 'Jose'

a.idade = 13
b.idade = 20

print("{} tem {} anos".format(a.nome, a.idade))
print("{} tem {} anos".format(b.nome, b.idade))
