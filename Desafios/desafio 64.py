#Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um numero [Para parar digite 999] :'))
    if num != 999:
        cont += 1
        soma += num
print('fim.\n Foram digitados {} números e a soma de todos é de {}'.format(cont, soma))