#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto !

preço = float(input(f'Digite aqui o valor do produto para saber seu desconto de 5%:'))

desconto = preço-preço*0.05 



print('O valor do pruduto com desconto de 5%, será de R${:.2f}'.format(desconto))