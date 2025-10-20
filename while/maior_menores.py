s_n = str('')
númer = int(input('Digite um número: '))
media = númer
maior = númer
menor = númer
c = 1
while s_n != 'n' and s_n != 'não':
    s_n = str(input('Quer continuar? [S/N]: ')).lower()
    if (s_n == 's') or (s_n == 'sim'):
        númer = int(input('Digite um número: '))
        media += númer
        c += 1
        if menor > númer:
            menor = númer
        if maior < númer:
            maior = númer
print('programa terminado')
print('Teve ao todo de {} números e sua média sendo {:.1f}'.format(c, media/c ))
print('Sendo maior valor {} e o menor {}'.format(maior, menor))
