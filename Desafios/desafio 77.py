palavras = ('aprender','estudar','aprimorar','ensinar','educar','conhecer','fazer','progredir','crescer','desenvolver','escolher','satisfazer','plantar','colher','correr')
for p in palavras:
    print(f'\nTemos a palavra {p} com as vogais: ', end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end='')