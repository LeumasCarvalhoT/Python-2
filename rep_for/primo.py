n = int(input('Informe um número: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='') 
        total += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(i), end='')

print('\033[m')
if total == 2:
    print('O total de números divisores é {}, logo o número é primo'.format(total))
elif total >= 3:
    print('[mO total de números divisores é {}, logo o número não é primo'.format(total))

   



