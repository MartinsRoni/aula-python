# Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista.

valores = []
mai = 0
men = 0
for cont in range(0,5):
    valores.append(int(input(f'Didite um valor para a posição {cont} : ')))
    if cont == 0:
        mai = men = valores[cont]
    else: 
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
