n = int(input('Digite um número: '))
#bin()
#hex()
#oct()
print('''Escolha uma dessas para converter seu número:
[1] BINÁRIO
[2] HEXADECIMAL
[3] OCTAL''')
opcao = int(input('Qual escolhe? '))

if opcao == 1:
    print('Seu número convertido para Binário fica assim: {}'.format(bin(n)[2:]))
elif opcao == 2:
    print('Seu número convertido para Hexadecimal fica assim: {}'.format(hex(n)[2:]))
elif opcao == 3:
    print('Seu número convertido para Octal fica assim: {}'.format(oct(n)[2:]))
else:
    print('Opção inválida.')
