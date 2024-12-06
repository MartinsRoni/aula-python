#Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

num = int(input('Digite um numero :'))
contador = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        contador = contador + 1         
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, contador))
if contador == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')

