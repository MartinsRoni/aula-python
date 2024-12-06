#Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre qual foi a média entre todos os valores e qual foi o maior e menor numero digitado. O programa deve perguntar para o usuário se ele quer ou não continuar a digitar os valores.

res = 'S'
cont = soma = media = maior= menor = 0
while res in 'Ss':
    num = int(input('Digite um valor:'))
    soma += num
    cont += 1
    if cont ==1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media = soma / cont
print('Voce digitou {} numeros e a média foi {}\n O maior numero foi {} e o menor foi {}'.format(cont, media, maior, menor))
    
    