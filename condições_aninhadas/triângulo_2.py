seg1 = int(input('Primeiro segmento: '))
seg2 = int(input('Segundo segmento: '))
seg3 = int(input('Terceiro segmento: '))
#if (seg1 == seg2 != seg3 or seg1 != seg2 == seg3 or seg1 == seg3!= seg2) :
        #print('O triângulo formado é Isósceles')
if (seg1 + seg2) > seg3 and seg1 < (seg2 + seg3) and (seg1 + seg3) > seg2:
    if seg1 == seg2 == seg3:
        print('O triângulo é Equilátero')
    elif seg1 != seg2 != seg3 != seg1 :
        print('O triângulo formado é Escaleno')
    else:
        print('O triângulo formado é Isósceles')
    
else:
    print('Não dá para formar um triângulo.')
    