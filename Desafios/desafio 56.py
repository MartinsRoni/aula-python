#Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo
somaidade = 0
mediaidade = 0
#qual o nome do homem mais velho
maioridadehomem = 0
nomevelho = ''
#Quantas mulheres tem menos de 20 anos
totmulher20 = 0


for p in range(1,5):
    print('-'*5, '{}º PESSOA'.format(p),'-'*5)
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade 
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        totmulher20 += 1
    mediaidade = somaidade/4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos, e se chama {}'.format(maioridadehomem, nomevelho))
print('E temos {} mulher com menos de 20 anos'.format(totmulher20))