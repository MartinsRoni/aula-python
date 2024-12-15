#Faça um programa que faça o computador pensar em um numero de 0 a 5 e peça para o usuário descobrir qual foi o numero selecionado pelo computador! O programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import choice

lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
usuario = int(input('Descubra o numero que eu estou pensando de 0 á 5:'))

if usuario == escolhido:
  print('Parabens, Voçê me venceu !!!.Eu pensei no numero {}'.format(escolhido))
else:
  print('Que pena, Voçê perdeu. Eu estava pensando no numero {}'.format(escolhido))