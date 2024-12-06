#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
#A) Quantas vezes apareceu o numero 9.
#B) Em que posição foi digitado o primeiro numero 3.
#C) Quais foram os numeros pares.

num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor : ')),
       int(input('Digite mais um valor : ')),
       int(input('Digite o ultimo valor: ')))
print(f'Voce digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 aparece na posição {num.index(3)+1}º')
else:
    print('Não foi encontrado o numero 3')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')

    