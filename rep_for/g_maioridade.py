import datetime
ano_atual = datetime.date.today().year
adulto = 0
menor = 0
for i in range(1, 8):
    gente = int(input('Informe a data de nascimento da {}º pessoa: '.format(i)))
    if ano_atual - gente >= 18:
        adulto += 1
    else:
        menor += 1

print('O total de pessoas maiores de idade é {}, e as que ainda vão chegar são {}'.format(adulto, menor))