from datetime import date 
nascimento = int(input('Informe sua data de nascimento: '))
atual = date.today().year
idade = atual - nascimento
if idade < 18:
    print('''Idade atual: {}
Idade necessária: {}
\033[32mNão chegou a idade indicada para o alistamento. A sua vez chegará em {}\033[m'''. format(idade, 18, atual + (18 - idade)))
    
elif idade == 18:
    print('''Idade atual: {}
Idade necessária: {}
\033[31mDeve ir se alistar IMEDIATAMENTE\033[m'''. format(idade, 18))
    
elif idade >= 18:
    print('''Idade atual: {}
Idade necessária: {}
\033[31mJá passou a dá data de alistamento, o ano foi {}\033[m'''. format(idade, 18, atual - (idade - 18)))
