#Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutula while

prim = int(input('Digite o termo: '))
raz = int(input('Digite a razão: '))
term = prim
cont = 1

while cont <= 10:
    print(' {} -> '.format(term), end=' ')
    cont += 1
    term += raz
print('Acabou')