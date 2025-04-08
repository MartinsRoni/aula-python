# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 
time = list()
jogador = dict()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['gols'] = []# Dicionário criado com uma lista vazia, para receber valores diferentes
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for cont in range(0, partidas):
        gols = int(input(f'Quantos Gols na partida {cont+1} ? '))
        jogador['gols'].append(gols)# Adicionando a Chave['gols'] os valores da variavel acima
        jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy()) 
    while True:
        res = str(input('Deseja adicionar mais jogadores: [S/N]? ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Digite somente S ou N. ')
    if res == 'N':
        break
print('-='*30)
print(f'cod ' ,end='')
for i in jogador.keys():
    print(f'{ i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):  
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-='*30)

while True:
    busca = int(input('Mostrar Dados de qual jogador? (999 Fim): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Não existe jogador com código {busca}')
    else:
        print(f'-- Levantamento de jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   Na partida {i+1} fez {g} gols')
    print('-='*30)
print('<<<- VOLTE SEMPRE ->>>')

