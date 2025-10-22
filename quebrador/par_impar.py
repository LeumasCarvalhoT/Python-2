import os
from random import randint
print("PAR OU ÍMPAR")
bot = randint(0, 10)
C = 0
while True:
    valor = int(input('Informe um número: '))
    p_i = str(input('Par ou ímpar [P/I]: ')).lower()
    os.system('cls')
    if (valor + bot) % 2 == 0:
        print('Você jogou {} e a máquina {}. O total é {}, PAR!'.format(valor, bot, valor + bot))
        if  p_i == 'p':
            print('VOCÊ GANHOU!')
            C += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif (valor + bot) % 2 != 0:
        print('Você jogou {} e a máquina {}. O total é {}, ÍMPAR!'.format(valor, bot, valor + bot))
        if  p_i == 'i':
            print('VOCÊ GANHOU!')
            C += 1
        else:
            print('VOCÊ PERDEU!')
            break
print('GAME OVER! Você venceu {} veze(s)'.format(C))



