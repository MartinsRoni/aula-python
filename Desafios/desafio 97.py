# Faça um programa que tenha uma função Escreva(), que recebe um texto qualquer como parametro e mostre uma mensagem com tamanho adaptável.
def escreva(texto):
    tam = len(texto) + 4
    print(f'~' * tam)
    print(f'{ texto:-^{tam}} ')
    print(f'~' * tam)

while True:
    texto = str(input('Didite um texto: '))
    escreva(texto)
    while True:
        res = str(input('Deseja continuar[S/N]: ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO. Digite somente S ou N')
    if res == 'N':
        break