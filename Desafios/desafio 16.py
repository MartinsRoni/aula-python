# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um numero : 6.127 tem a parte inteira: 6

from math import floor, ceil
num = float(input('Digite um numero qualquer para saber sua parte inteira:'))

print('O numero {}, tem sua parte inteira {}'.format(num, floor(num)))
