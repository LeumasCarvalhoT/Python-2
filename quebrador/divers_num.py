soma = 0 
c = 0
while True:
    n = int(input('Digite um algum valor (digite 999 para parar): '))
    if n == 999:
        break
    soma += n
    c +=1
print('A soma dos {} valores digitados é {}.'.format(c, soma))