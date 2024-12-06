#Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas não atingiram a maioridade e quantas ja são maiores (21 anos)
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pessoas in range(1,8):
    nasc = int(input('Em que ano a {}º nasceu:'.format(pessoas)))
    idade = atual - nasc  
    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print('Tivemos {} pessoas maior de idade '.format(totmaior))
print('E também tiveos {} pessoas menores de idade'.format(totmenor))




    