import random
import time
import os
bot = random.randint(0, 2)
pc = ''
if bot == 0:
    pc = 'PEDRA'
elif bot == 1:
    pc = 'PAPEL'
elif bot == 2:
    pc = 'TESOURA'

print('''[0] PEDRA
[1] PAPEL
[2] TESOURA''')
escolha = int(input('Qual será a jogada? '))
hum = ''
if escolha == 0:
    hum = 'PEDRA'
elif escolha == 1:
    hum = 'PAPEL'
elif escolha == 2:
    hum = 'TESOURA'
os.system('cls')
time.sleep(0.5)
print('PEDRA')
time.sleep(0.5)
print('PAPEL')
time.sleep(0.5)
print('E TESOURA')
print()

if escolha == 0 or escolha == 1 or escolha == 2:
    if escolha == bot and bot == escolha:
        print('EMPATE!!!')
        print('''JOGADOR, JOGADA: {}. 
COMPUTADOR, JOGADA: {}.'''.format(hum, pc))
    elif (escolha == 1 and bot == 0) or (escolha == 0 and bot == 2) or (escolha == 2 and bot == 1):
        print('''JOGADOR VENCEU, JOGADA: {}. 
COMPUTADOR PERDEU, JOGADA: {}.'''.format(hum, pc))
    else:
        print('''COMPUTADOR VENCEU, JOGADA: {}.
JOGADOR PERDEU, JOGADA: {}.'''.format(pc, hum ))
