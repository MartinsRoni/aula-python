# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programador vai perguntar quantos jogos serão registrados
#  e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tud o em uma lista composta..

import random
from time import sleep
lista = list(range(1,60))
print('-' *30)
print('      JOGO DA MEGA SENA     ')
print('-' *30)
num = int(input('Quantos números da Sorte você gostaria?: '))
print(f'<'*5, 'Sorteando  Jogos', '>'*5)

for cont in range(0, num):
    jogo = random.sample(lista, 6)
    jogo.sort()
    sleep(2)
    print(f'Jogo {cont+1} {jogo}')
print('-=' *5, '<BOA SORTE>', '=-'* 5)