n = int(input('Digite um número para fazer um tabuada: '))

for i in range(1, 11):
    print('{} x {:>2} = {}'.format(n, i, i * n))