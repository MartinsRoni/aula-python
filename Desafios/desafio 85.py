#Crie um programa que o usuário possa digitar sete valores numéricos e cadastre-os em uma lista unica 
# que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente. 
#OBS: Lista principal com duas listas dentro separando valores impares de pares

lista = [[], []]


for cont in range(1, 8):
    n = int(input(f'Digite o {cont}°. valor: '))
    if n %2 == 0:
        lista[1].append(n)
    else:
        lista[0].append(n)
lista[0].sort()        
lista[1].sort()

print(f'Os valores Impares digitados foram: {lista[0]}')
print(f'Os valores Pares digitados foram: {lista[1]}')