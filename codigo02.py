class Pessoa:
    pass

qtd = int(input('Quantas pessoas?'))
pessoas = []

i = 0
while i < qtd:
    p = Pessoa()
    p.nome = input('Digite o nome: ')
    p.idade = int(input('Digite a idade: '))
    pessoas.append(p)
    i = i + 1

print("\n\n")

for p in pessoas:
    print("{} tem {} anos".format(p.nome, p.idade))    

   