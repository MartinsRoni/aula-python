#Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista. No final mostre :
#A) Quantas pessoas foram cadastradas B)Uma listagem com as 2 pessoas mais pesadas C)Um listagem com as 2 pessoas mais leves.
pessoas = list()
dados = list()
mai = men = 0


while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]

    if continuar == 'N':
        print('Cadastros finalizados')
        break

print(f'Você registrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f' {p[0]}', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
         print(f' {p[0]}', end='')
print()

