#Crie um programa que leia vários numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999 que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles desconsiderando o flag.
n = soma = cont = 0

while True:
    n = int(input('Digite um numero [999 para encerrar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
    
print(f'Foram inseridos {cont} valores!\n E a soma de todos os valores é de {soma}')
print('Fim do Programa')