# Melhore o jogo do desafio 28 onde o cumputador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.

from random import choice

lista = [0,1,2,3,4,5,6,7,8,9,10]
computador = choice(lista)
contador = 0
jogador = int(input('Descubra o numero que o computadoe esta pensando entre 0 á 10:'))

while jogador != computador:
    jogador = int(input('Voçe errou, o cumputador não escolheu {}. Tente novamente:'.format(jogador)))
    contador = contador + 1
print('Parabens você acertou! O computador escolheu {},e você precisou chutar {} vezes! '.format(computador, contador)) 