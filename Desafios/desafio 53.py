#crie um programa que leia uma frase qualquer e diga se ela é uma PALINDROMA, desconsiderando os espaços.
#Ex: (APOS A SOPA ), (A SACADA DA CASA ), (A TORRE DA DERROTA), ( O LOBO AMA O BOLO ), (ANOTARAM A DATA DA MARATONA) *TIRAR ESPAÇOS

frase = str(input('Digite uma frase:')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
inverso = junto[::-1]#fatiamento

'''for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]'''#jeito de fazer com for
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A palavra digitada, não é um PALÍNDROMO')

