# Crie um programa onde 4 jogadores jogem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esses dicionários em ordem, sabendo que o vencedor tirou o maior numero no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = list()
sleep(1)
print('-='*10, 'Dados Lançados', '=-'*10)

for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)#(1)Referencia por valor, (0)referencia por chave, e reverse=True inverte o sentido da ordem Sorted
sleep(1)
print('*'*10, 'RANKING', '*'*10 )

for i, v in enumerate(ranking):#Usando enumerate pois ranking é tratada como lista
    print(f'  {i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)

