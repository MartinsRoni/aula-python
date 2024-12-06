#Crie um programa que leia um nome de uma cidade e diga se ela começa ou nao com o nome "santo"

cidade = str(input('Digite o nome da cidade:')).strip()
#[:5] para saber se começa 
print(cidade[:5].upper() == 'SANTO')