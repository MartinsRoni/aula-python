#Faça um programa que tenha uma lista chamada numeros e duas funções chamadas Sorteio() e SomaPar(). A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
import random
numeros = list(range(0,51))
def sorteio(numeros):
    print(numeros)



sorteio(random.sample(numeros, 5))


def Somapar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'{s} ')


Somapar()


