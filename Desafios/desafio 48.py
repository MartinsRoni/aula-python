#Faça um programa que calcule a soma entre todos os numeros impares que são mutiplos de tres e que se encontram no intervalo de 1 até 500.

soma = 0 
cont = 0

for c in range(1,501,2):
    if c % 3 == 0:
        soma += c #simplificado 
        cont = cont + 1 #normal
print('A soma de todos os {} valores solicitados é de {}'.format(cont,soma))