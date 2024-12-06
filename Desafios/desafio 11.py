#faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m**2!

altura = int(input('Digite a altura de sua parede:'))
largura = int(input('Digite a largura de sua parede:'))

area = altura*largura
litros = area/2
print('Sua parede mede {} metros quadrados, e voce necessitara de {} litros de tinta, para pinta-la !'.format(area, litros))