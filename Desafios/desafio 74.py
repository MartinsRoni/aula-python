#Crie um programa que vai gerar 5 numeros aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de numeros gerados e também qual o maior e menor numero gerado 
from random import randint

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os numeros sorteados foram: ',end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior numero gerado foi {max(num)} e o menor foi {min(num)}')