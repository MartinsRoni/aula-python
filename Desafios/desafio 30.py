#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

num = int(input('Digite um numero para saber se ele é impar ou par:'))
resu = num % 2
if resu == 0:
 print('O numero {}, é um numero PAR '.format(num))
else:
 print('O numero {}, é um numero IMPAR'.format(num))
print(resu)
        




