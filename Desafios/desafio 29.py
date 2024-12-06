#Escreva um programa que leia a velocidade de um carro. se ele utrapassar 80km/h, mostre uma mensagem que ele foi mutado. A multa vai custar R$7,00 por cada km acima do limite 

velocidade = int(input('Qual a velocidade do carro?'))
multa = (velocidade - 80)*7
if velocidade >= 80: 
    print('Você ultrapassou o limite da via e foi multado em R${:.0f},00'.format(multa))
else:
    print('Dirija com cuidado!')