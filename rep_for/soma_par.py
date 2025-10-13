soma = 0

for i in range(1, 7):
    n = int(input('Digite o {}º número: '.format (i)))
    if n % 2 == 0:
        soma += n
print('A soma total dos números pares é {}'.format(soma))
    
