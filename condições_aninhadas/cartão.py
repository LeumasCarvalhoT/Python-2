import os
dimdim = float(input('Informe o quanto vai pagar pelo(s) produto(s): R$'))
print('''[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual o senhor(a) vai preferir? '))


os.system('cls')
if opcao == 1:
    desc = dimdim - dimdim * 10/100
    print('O valor total a pagar é de R${:.2f}, tenha um bom dia.'.format(desc))
elif opcao == 2:
    desc = dimdim - dimdim * 5/100
    print('À vista no cartão, fica R${:.2f}.'.format(desc))
elif opcao == 3:
    parcelas = int(input('Por quanto parcelará? '))
    print('Cada a parcela será de R${:.2f} e ao todo R${:.2f}'.format(dimdim/2, dimdim))
elif opcao == 4:
    parcelas = int(input('Por quanto parcelará? '))
    desc = dimdim + dimdim * 20/100
    if parcelas >= 3:
        print('Cada parcela será de R${:.2f}, com o todo de R${:.2f}'.format(desc / parcelas, desc))
    else:
        print('Só permitido de 3x ou mais parcelas!')
else:
    print('Opção inválida.')
