#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

real = float(input('Quanto dinheiro voce tem na sua carteira?:R$'))
dollar = real / 5.20

print('Voçe tem R${:.2f} na sua carteira, e pode comprar US${:.2f} '.format(real, dollar))