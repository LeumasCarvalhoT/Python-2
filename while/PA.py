print('Gerador PA')
termo = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
c = 0
while c != 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    c += 1
print('FIM')
