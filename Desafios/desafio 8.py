#Escreva um programa que leia um valor em metros e converta em centimetros e milimetros!
metro = int(input('Digite aqui o valor em metros:'))
cent = metro*100
mili = metro*1000

print('O valor de {} metros, é equivalente a {} centimetros e {} milimetros !'.format(metro, cent, mili))