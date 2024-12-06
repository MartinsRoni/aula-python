#Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0

for num in range(0,6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma+num
        cont = cont+1
print('Foram analizados {} numeros pares, e a soma de todos eles é de {} '.format(cont,soma))


    

    
