#Crie um programa que faça o computador jogar Jokenpo com vc

from random import randint 
from time import sleep
import emoji
itens = ('pedra','papel','tesoura')
computador = randint(0,2)

print('''Suas opções:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO!!!')
sleep(2)
print('=-'*12)
if computador == 0:
   print(emoji.emojize('O computador jogou {}:oncoming_fist:'.format(itens[computador])))
elif computador == 1:
   print(emoji.emojize('O computador jogou {}:hand_with_fingers_splayed:'.format(itens[computador])))
else:
   print(emoji.emojize('O computador jogou {}:victory_hand:'.format(itens[computador])))
if jogador == 0:
   print(emoji.emojize('Voçê jogou {}:oncoming_fist:'.format(itens[jogador])))
elif jogador == 1:
    print(emoji.emojize('Voçê jogou {}:hand_with_fingers_splayed:'.format(itens[jogador])))
elif jogador == 2:
    print(emoji.emojize('Voçê jogou {}:victory_hand:'.format(itens[jogador])))
else:
    print('JOGADA INVALIDA. JOGUE NOVAMENTE')
print('-='*12)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print(emoji.emojize('JOGADOR VENCEU !!!'))
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')

    else:
        print('jOGADA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')    
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
        