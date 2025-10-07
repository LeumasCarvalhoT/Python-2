casa = float(input('Quanto é a casa em R$? '))
sal = float(input('Seu salário: '))
anos = int(input('E em quantos anos você pretende financiar a casa? '))
prestaçao = casa / (anos * 12)

if prestaçao > (sal * 30/100):
    print('\033[31mO seu salário não dá conta de pagar a casa nesse tempo.' \
    'Tenha um bom dia.\033[m')
elif prestaçao <= (sal * 30/100):
    print('\033[32mO salário é o suficiente, aceitaremos fazer o empréstimo.\033[m')

print("""Com o valor da casa sendo R${:.2f} com o tempo de {} anos,
    o emprestimo mensal é de R${:.2f}""".format(casa, anos, prestaçao))