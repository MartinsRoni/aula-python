#Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias concecutivas que ele conquistou no final do jogo.
from random import randint
v = 0

print('=-'*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*12)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar[P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end=' ')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu')    
            v += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if total % 3 == 0:
            print('Voce Venceu')
            v +=1
        else:
            print('Voce Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')