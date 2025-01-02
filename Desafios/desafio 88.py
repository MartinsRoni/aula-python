# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programador vai perguntar quantos jogos serão registrados
#  e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta..

import random
from time import sleep
lista = list(range(1,60))
print('-' *30)
print('      JOGO DA MEGA SENA     ')
print('-' *30)
num = int(input('Quantos números da Sorte você gostaria?: '))
print(f'<'*5, 'Sorteando  Jogos', '>'*5)

for cont in range(0, num):
    jogo = random.sample(lista, 6)#seleciona 6 elementos aleatórios da lista listasem repetições.
    jogo.sort()# O método sort()ordena os elementos da lista jogoem ordem crescente.
    sleep(2)
    print(f'Jogo {cont+1} {jogo}')
print('-=' *5, '<BOA SORTE>', '=-'* 5)