#Refaça o desafio 9 mostrando a tabuada que o usuário escolher, so que agora usando o laço for.

tab = int(input('Digite um numero para saber a sua tabuada:'))

for c in range(1,11):
    print('{} x {:2} = {}'.format(tab, c, tab*c))
    
