#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triangulo.

segA = float(input('\033[0;34mPrimeiro segmento:\033[m'))
segB = float(input('\033[0;35mSegundo segmento:\033[m'))
segC = float(input('\033[0;36mTerceiro segmento:\033[m'))

if segA + segB > segC and segB + segC > segA and segA + segC > segB:
    print('\033[0;32mOs segmentos podem formar um triangulo\033[m')
else:
    print('\033[0;31mOs segmentos não podem formar um triangulo\033[m')