# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final tudo isso sera guardado em um dicionário, incluindo o total de gols que ele fez na temporada.

jogador = dict()
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['gols'] = []# Dicionário criado com uma lista vazia, para receber valores diferentes
partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for cont in range(0, partidas):
    gols = int(input(f'Quantos Gols na partida {cont+1} ? '))
    jogador['gols'].append(gols)# Adicionando a Chave['gols'] os valores da variavel acima
print('-='*30)
jogador['total'] = sum(jogador['gols'])
for k, v in jogador.items():
    print(f'  - O campo {k} tem valor {v}  ')
print('-='*30)
print(f'O jogador {jogador['nome']}, jogou {partidas} partidas. ')
for i, v in enumerate(jogador["gols"]):
    print(f'  => Na partida {i+1}º O jogador {jogador["nome"]} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
