termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for i in range(0, 10):
    print('{} '.format(termo1), end='-> ')
    termo1 += razao
print('ACABOU!', end=' ')