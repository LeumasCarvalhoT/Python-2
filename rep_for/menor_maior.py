humano = float(input('Informe o peso da 1º pessoa: '))
maior = 0
menor = humano
for i in range(2, 6):
    humano = float(input('Informe o peso da {}º pessoa: '.format(i)))
    if humano > maior:
        maior = humano
    if humano < menor:
        menor = humano
print('A pessoa com maior peso tinha {}Kg e a menor {}Kg.'.format(maior, menor))

