sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Por favor, Informe seu sexo: '))
if sexo == 'M':
    print('Sexo Masculino arquivado.')  
if sexo == 'F':
    print('Sexo Feminino arquivado.')
       
        
    
      