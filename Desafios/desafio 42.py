#Refaça o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado: -Equilátero: todos os lados igais. -Isosceles: Dois lados iguais. -Escaleno: todos os lados diferentes.

segA = float(input('Digite o seguimento A:'))
segB = float(input('Digite o seguimento B:'))
segC = float(input('Digite o seguimento C:'))

if segA+segB > segC and segB+segC > segA and segA+segC > segB:
    print('Os seguimentos podem formar um triangulo ',end='')
    if segA == segB == segC:
        print('Equilátero')
    elif segA != segB != segC != segA:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('\033[0;31mOs segmentos não podem formar um triangulo\033[m')