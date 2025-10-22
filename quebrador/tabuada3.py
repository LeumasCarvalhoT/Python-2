import os
while True:
    tab = int(input('Quer uma tabuada de qual número?: '))
    if tab < 0:
        print('Programa encerrado devido ao valor negativo!')
        break
    os.system('cls')
    for i in range(1, 11):
        print('{} x {} = {}'.format(tab, i, tab*i))
    