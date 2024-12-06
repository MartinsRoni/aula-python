#Faça a um programa que mostre a tabuada de vários numeros, um de cada vez para cada numero digitado pelo usuário. O programa será interrompido quando o numero solicitado for negativo.
tab = 0
while True:
    tab = int(input('Quer saber a Tabuada de qual numero? '))
    print('='*37)
    if tab < 0:
        break
    for c in range(1,11):
        print('{:2} x {:2} = {}'.format(c, tab, c*tab))
    print('='*37)
print('Programa finalizado!')