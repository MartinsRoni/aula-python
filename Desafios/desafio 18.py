#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno cosseno e tangente desse angulo.
import math 

angulo = float(input('Digite o Ângulo desejado: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O Angulo de {} \nTem o Seno {:.2f} \nO Coseno {:.2f} \nE a Tangente{:.2f}'.format(angulo, seno, coseno, tangente))