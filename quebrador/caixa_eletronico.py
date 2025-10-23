print('Banco CEV')
sacamento = float(input('Quanto você quer sacar?: '))
l = 50
xx = 20
x = 10
v = 5
i = 1
cl = cxx = cx = cv = ci = 0
cel = 0
while cel != sacamento:
    if (cel + l) < sacamento:
        cel += l
        cl += 1
    elif(cel + xx) < sacamento:
        cel += xx
        cxx += 1
    elif (cel + x) < sacamento:
        cel += x
        cx += 1
    else:
        cel += i
        ci += 1
if cl >= 1:
    print('O total de cédulas de R$50 usadas foi de {}'.format(cl))
if cxx >= 1:
    print('O total de cédulas de R$20 usadas foi de {}'.format(cxx))
if cx >= 1: 
    print('O total de cédulas de R$10 usadas foi de {}'.format(cx))
if cv >= 1:
    print('O total de cédulas de R$5 usadas foi de {}'.format(cv))
if ci >= 1:
    print('O total de moedas de R$1 usadas foi de {}'.format(ci))

    
