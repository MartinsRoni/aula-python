#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade: -Até 9 anos: Mirim. -Até 14 anos: Infantil. -Até 19 anos: Junior. -Até 20 anos: Senior. -Acima: Master
from datetime import date

ano = int(input('Insira o ano de seu nascimento:'))
idade = date.today().year - ano

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 20:
    print('Categoria Senior')
else:
    print('Categoria Master')