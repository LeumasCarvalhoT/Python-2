import os
n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
opcaos = 0
while opcaos != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa''')
    opcaos = int(input("O que vai querer agora? prefere?: "))
    os.system('cls')
    if opcaos == 1:
        print('A soma entre {} e {} é = {}'.format(n1, n2, n1+n2))
    elif opcaos == 2:
        print('A multiplicação entre {} e {} é = {}'.format(n1, n2, n1*n2))
    elif opcaos == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n2))
    elif opcaos == 4:
        print('Renove os valores:')
        n1 = int(input('1° valor: '))
        n2 = int(input('2° valor: '))
print('O programa terminou.')



