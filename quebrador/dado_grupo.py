import os
print('CADASTRE UMA PESSOA')
opc = 's'
c = f = m = 0
while True:
    if opc == 's' or opc == 'sim':
        idade = int(input('Idade: '))
        sex = str(input('Sexo [M/F]: ')).lower()
        if idade >= 18:
            c += 1
        elif sex == 'm':
            m += 1
        elif sex == 'f' and idade < 20:
            f += 1
    if opc == 'n' or opc =='não':
        break
    opc = str(input('Gostaria de continuar?[S/N]: ')).lower()
    os.system('cls')
print('''Total de pessoas com mais de 18 anos: {}
Temos {} homens cadastrados.
E {} mulheres com menos de 20 anos.'''.format(c, m, f))
