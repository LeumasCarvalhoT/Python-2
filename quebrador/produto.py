import os
print('Loja Baratão')
nome = str(input('Nome do produto: '))
preco = float(input('O preço do produto: '))
produto = nome
menor = soma = mil = preco
c = 0
while True:
    continua = str(input('Continuar?[S/N]: ')).lower()
    os.system('cls')
    if continua == 's' or continua == 'sim':
        nome = str(input('Nome do produto: '))
        preco = float(input('O preço do produto: '))
        soma += preco
        mil = preco
        if preco < menor:
            menor = preco
            produto = nome
        elif mil >= 1000:
            c += 1
    if continua == 'n' or continua == 'não':
        break
print('''O total a se pagar será de {:.2f}
Temos {} produtos custando mais de R$1000.00
O produto mais barato foi {}, que custa R${}'''.format(soma, c, produto, menor))


            

