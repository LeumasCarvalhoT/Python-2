import os
media = 0
mais_velho = 0
memoria = 0
mocinha = 0
for i in range(1, 5):
    print('==== {}ª PESSOA ===='.format(i))
    nome = (input('Nome: '))
    idade = int(input('Idade: '))
    media += idade/4
    Sex = (input('Sexo [M/F]: '))
    os.system('cls')
    if (Sex == 'm' or Sex == 'M') and idade > mais_velho:
        mais_velho = idade
        memoria = nome
    if (Sex == 'F' or Sex == 'f') and idade < 20:
        mocinha += 1

print('A média de idade do grupo é de {}'.format(media))
if mais_velho != 0:
    print('O homem mais velho tem {} anos e chama-se {}'.format(mais_velho, memoria))
else:
    print('Não há homens nesse grupo.')
print('No total há {} mulher(es) com menos de 20 anos.'.format(mocinha))