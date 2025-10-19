print('Gerador PA')
termo = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
meta = 10
c = 0
while c != meta:
    if c != meta - 1: 
        print('{} -> '.format(termo), end='')
    else: 
        print('{} -> PAUSA'.format(termo), end='')
    termo += raz
    c += 1
    if c == meta:
        print()
        mais = int(input('Quer continuar? Se sim, por quanto mais?: '))
        if mais != 0:
            meta += mais
        else:
            meta += 0
print('Progressão finalizada com {} termos mostrados.'.format(c))
