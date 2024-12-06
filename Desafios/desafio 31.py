#Desenvolva um programa que pergunte a distançia de uma viagem em km. Calcule o preço da passagem, cobrando  R$0,50 por km para viagens de até 200km e RS0,45 para viagens mais longas 

distancia = int(input('Qual é a distância de sua viagem em Km?'))
custo1 = distancia*0.50
custo2 = distancia*0.45

if distancia <=200:
    print('Sua passagem custara R${:.0f},00'.format(custo1))
else:
    print('Conseguimos uma condição especial para você, e sua passagem custara R${:.0f},00'.format(custo2))