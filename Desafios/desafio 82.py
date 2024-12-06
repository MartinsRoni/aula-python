#Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso, crie duas lista extras que vão conter apenas os valores pares e os impares digitados, respectivamente. Ao final mostre o conteudo das 3 listas geradas.

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um numero: ')))
    
    res = str(input('Deseja continuar? [S/N]: '))
    if res in 'Nn':
        break
for i, v in enumerate(num):
    if v %2 == 0:
        pares.append(v)
    elif v %2 == 1:
        impares.append(v)
print(f'A lista completa é {num}')
print(f'A lista dos pares é {pares}')
print(f'A lista dos impares é {impares}')