# Faça um programa que tenha uma função Maior(), que receba vários parametros com valores inteiros. Seu programa tem que analizar todos os valores e dizer qual deles foi o maior digitado.
from time import sleep

def maior(* num):
    cont = mai = 0
    print('-='* 20)
    print('Analizando os valores ...')
    for valor in num:
        print(f'{valor}   ', end='', flush=True)    
        sleep(0.3)
        if cont == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        cont += 1
    print(f'\nForam informados {cont} valores.')
    print(f'O maior valor informado foi {mai}.')

maior(5, 7, 1, 9, 4, 2, 16)
maior(5, 9, 25, 2)
maior(3, 1)
maior(8)
maior()

