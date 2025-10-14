oração = str(input('Digite um frase: ')).strip().upper()
sem_ = oração.split()
j = ''.join(sem_)
invertido = j[::-1]
if invertido == j:
    print('O inverso de \033[32m{}\033[m, é um palíndromo: \033[33m{}\033[m.'.format(oração, invertido))
else:
    print('O inverso de \033[31m{}\033[m, não é palíndromo: \033[33m{}\033[m.'.format(oração, invertido))