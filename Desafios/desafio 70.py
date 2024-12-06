#Crie um programa que leia o nome e o preço de vários produtos. O programa devera perguntar se o usuário deseja continuar. No final mostrar:
#1.Quál é o total gasto na compra - 2.Quantos produtos custam mais de R$1000.00 - 3. Qual o nome do produto mais barato.

totalGasto = maisbarato = mais1000 = nomeP = cont = 0
nomemaisbarato = ''


while True:
    nomeP = str(input('Nome do produto: '))
    preço = int(input('Valor do Produto R$: '))
    cont += 1
    totalGasto += preço
    if preço >= 1000:
        mais1000 += 1
    if cont == 1:
        maisbarato = preço
        nomemaisbarato = nomeP
    else:
        if preço < maisbarato:
            maisbarato = preço
            nomemaisbarato = nomeP    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar == 'N':
        print('Lista de produtos fechada.')
        break
print(f'O total gasto foi de RS {totalGasto},00. \nHá {mais1000} produtos custando mais de R$1000,00.\nE o pruduto mais barato foi  {nomemaisbarato}, custando R${maisbarato},00')
    