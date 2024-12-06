#Crie um programa que leia 2 valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos numeros 
#[5]sair do programa 
#Seu programa devera realizar a operação desejada em cada caso
from time import sleep

num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digirte o segundo numero:'))
opcao = 0
soma = num1 + num2
mult = num1 * num2
while opcao != 5:
    print('''
[1]Somar
[2]Mutiplicar
[3]Maior
[4]Novos numeros
[5]Sair do programa''')
    opcao = int(input('>>>>>>Qual é sua opção?:'))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    if opcao == 2:
        print('{} x {} é {}'.format(num1,num2,mult))
    if opcao == 3:
        if num1 > num2:
            print('Entre {} e {} o maior é {}'.format(num1,num2,num1))
        else:
            print('Entre {} e {} o maior é {}'.format(num1,num2,num2))
    if opcao == 4:
        print('Digite os numero novamente:')
        num1 = int(input('Primeiro valor:'))
        num2 = int(input('Segundo valor:'))
    if opcao == 5:
        print('Finalizando ...')
        sleep(3)
print('Fim do programa, volte sempre!')
