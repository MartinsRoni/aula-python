
#Faça um programa que leia o sexo de uma pessoa, mas so aceite M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto


sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]  
while sexo not in  'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe os dados corretamente:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))



 
