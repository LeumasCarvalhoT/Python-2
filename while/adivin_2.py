import time
import random
#inspirado no Guanabara
pc = random.randint(0, 10)
cont = 0
acertou = False
print('Ola, sou teu computador...')
time.sleep(1)
print('Pensei agora em um número entre 0 e 10')
print('Consegue adivinhar? Então tente!')
player = int(input('O que você sugere?: '))
cont += 1
while not acertou:
    cont += 1
    if player < pc:
        player = int(input('Maior... tem mais uma chance: '))
    else:
        player = int(input('Menor... tem mais uma chance: '))
    if player == pc:
       acertou = True
print('Acertou depois de {} tentativas. Parabéns'.format(cont))

#A mais simples para mim
#hipotese = int(input('Qual sua hipótese?: '))
#cont += 1
#while hipotese != pc:
    #cont += 1
    #if hipotese < pc:
       #hipotese = int(input('Maior... tem mais uma chance: '))
   #else:
        #hipotese = int(input('Menor... tem mais uma chance: '))
#print('Acertou depois de {} tentativas. Parabéns.'.format(cont))#
