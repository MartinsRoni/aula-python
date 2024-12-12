# Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]   
spar = scol = mai = 0

for l in range(0,3):# As três primeiras linhas estão recebendo os valores para as matrizes
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um valor para matriz:'))
print('=-'*30)
for l in range(0,3):# As três ultimas linhas estão estruturando a forma a ser exibida
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 == 0:    
            spar += matriz[l][c]  
    print()
print('=-'*30)
print(f'A Soma de todos os valores pares digitados é de :{spar}')
for l in range(0,3):# Somando apenas a terceira coluna  
    scol += matriz[l][2]
print(f'A soma de todos os valores da terceira coluna é de :{scol}')
for  c in range(0,3):# Verificando o maior numero da segunda linha
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c]> mai:
        mai = matriz[1][c]
print(f'E o maior valore da segunda coluna é de :{mai}')
