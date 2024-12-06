#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji

print('CONTAGEM REGRESIVA PARA QUEIMA DE FOGOS!!!')
sleep(3)
print('VAmos lá ?')
sleep(3)
for c in range(10, -1,-1):
    print(c)
    sleep(1)
print(emoji.emojize(':sparkles:,:confetti_ball:'))