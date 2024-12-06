#Crie um programa que leia vários números e coloque-os em uma lista. Depois mostre: A)Quantos numeros foram digitados B)A lista de forma ordenada em ordem decrescente C)Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0

while True:
    n = int(input('Digite um numero :'))
    lista.append(n)
    cont += 1 #posso usar len(lista) no print para ter o mesmo resultado
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).strip().upper()[0]
                                                                             
    if continuar == 'N':
        print('Finalizado')
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} números')
print(f'Os números digitados foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
