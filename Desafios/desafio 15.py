#Escreva um programa que a quantidade de km percorridos por um carro alugado e a quantidade de dias pela qual ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado

km = float(input('Imforme quantos quilometros voçe rodou com o carro:'))
dias = float(input('informe quantos dias voçe utilizou o carro:'))

preço = km*0.15 + dias*60.00
print ('O valor a pagar é de: R${:.2f}'.format(preço))