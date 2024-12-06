#Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que ele quer mostrar 0 termos.

prim = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a Razão: '))
cont = 1
term = prim
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {} ->'.format(term), end='')
        cont += 1
        term = term + raz
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Fim\n Progreção finalizada com {} termos mostrados'.format(total))