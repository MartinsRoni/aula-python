# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

#Formula- A**2 = B**2 + C**2
from math import hypot

catOp = float(input('Digite o Cateto Oposto:'))
catAd = float(input('Digite o Cateto Adjacente:'))

'''hipo  = (catOp**2 + catAd**2) ** (1/2)'''
hipo = hypot(catOp, catAd)
print('O comprimento da Hipotenusa resultante das somas dos catetos é {:.2f} '.format(hipo))


