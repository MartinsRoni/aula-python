#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno, individualmente.

ficha = list()
resu = list()


while True:
    nome = (str(input('Nome: ')))
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    r = 0
    

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='* 20)
print(f'{'Nº.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'* 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}') 
print('-'* 30)
while True:
    r = (int(input('Mostrar notas de qual aluno? [999 p/ interromper]: ')))
    if r == 999:
        print('FINALIZANDO...')
        break
    if r <= len(ficha) -1:
        print(f'As notas de {ficha[r][0]} foram {ficha[r][1]}')
print('<<<<<<<<<<- VOLTE SEMPRE ->>>>>>>>>>')
    



