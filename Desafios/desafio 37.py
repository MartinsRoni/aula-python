#Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para Binário 2 para Octal 3 para Hexadecimal

num = int(input('Digite um numero inteiro:'))
print('''Escolha a base para converção
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
escolha = int(input('Escolha a converção:'))

if escolha == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('O numero digitado não é uma das opções. Tente novamente!')