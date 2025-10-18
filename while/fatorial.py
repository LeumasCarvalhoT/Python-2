fatorial = int(input('Digite um número para o fatorial: '))
soma = fatorial
print('calculando {}! ='.format(fatorial), end='')
while fatorial != 1:
    print(' {} x'.format(fatorial), end='')
    soma *= fatorial - 1
    fatorial -= 1
print(' {} = {}'.format(1, soma), end='')