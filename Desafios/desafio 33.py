#Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor 
num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
num3 = int(input('Digite o terceiro numero:'))
#Analizando quem é o menor 
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
print('O menor numero digitado foi {}'.format(menor))
#Analizando quem é o maior 
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O maior numero digitado foi {}'.format(maior))