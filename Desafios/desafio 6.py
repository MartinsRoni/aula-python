#Crie um algoritimo que leia um numero e mostre seu dobro, triplo e raiz quadrada  !

num = int(input('Digite um numero para saber seu dobro, triplo e raiz quadrada:'))
dobro = num*2
triplo = num*3
raiz = num**(1/2)

print('O dobro de {} é {}, seu triplo {}, e sua raiz quadrada é {}.'.format(num, dobro, triplo, raiz))