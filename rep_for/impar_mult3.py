cont = 0
soma = 0

for i in range(3, 500, 3):
    if i % 2 == 1:
        cont += 1
        soma = soma + i

print('A soma de todos os {} valores ímpares, multiplos de 3, é igual {}'.format(cont, soma))