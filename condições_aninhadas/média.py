nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
med = (nota1 + nota2) / 2

if med < 5:
    print('Você foi reprovado')
elif med >= 5 and med <= 6.9:
    print('Você está em Recuperação')
elif med >= 7:
    print('Você foi Aprovado, se orgulhe.')
print('Sua média é', med)
