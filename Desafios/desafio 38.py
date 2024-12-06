#Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem: -O primeiro valor é maior. - O segundo valor é maior. - Não existe valor maior, os dois são iguais.

num1 = int(input('Digite o primeiro numero inteiro:'))
num2 = int(input('Digite o segundo numero inteiro:'))
print( 'ANALIZANDO')

if num1 > num2:
    print('O primeiro valor de {}, é maior que o segundo valor de {} !'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor de {}, é maior que o primeiro valor de {} !'.format(num2, num1))
else:
    print('Os dois numeros são iguais')
