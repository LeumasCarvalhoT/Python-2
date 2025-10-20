i = soma = c = 0
while i != 999:
    número = int(input('Digite um número [999 para parar]: '))
    i = número
    if i != 999:
        soma += i
        c += 1
print('Você digitou {} números. A soma total entre esses números é de {}'.format(c, soma))