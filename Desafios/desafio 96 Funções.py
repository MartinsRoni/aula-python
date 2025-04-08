# Faça um programa que tenha uma função chamada Área() que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a Área do terreno. 

def area(larg, compr):
    area = larg * compr
    print(f'A área de um terreno de {larg}m x {compr}m é de {area}m')
       
print('-' * 20)
print('Controle de Terrenos')
print('-' * 20)
larg = float(input('Largura (m): '))
compr = float(input('Comprimento (m): '))
area(larg, compr)
