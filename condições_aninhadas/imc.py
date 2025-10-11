import os
kg = float(input('Informe seu peso: '))
alt = float(input('Informe sua altura: '))
imc = kg / (alt**2)

os.system('cls')
if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Está ABAIXO DO PESO normal!.')
elif imc >= 18.5 and imc < 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Está com o peso ideal.')
elif imc >= 25 and imc < 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Ela está com sobrepeso.')
elif imc >= 30 and imc < 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Ela está com OBSEDIDADE!.')
else:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Ela está com OBSEDIDADE GRAVE!, busque ajuda imediatamente.')