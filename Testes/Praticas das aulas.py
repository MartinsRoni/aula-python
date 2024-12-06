# Refazendo desafio 81
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar ? [S/N]: '))
    if res in 'Nn':
        break
print(f'Voce digitou {len(lista)} valores')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista!')


