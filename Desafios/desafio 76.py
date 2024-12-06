#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia. No final mostre uma listagem de preços, organizando os dados em forma tabular 

lista = ('Arroz', 26.90,'feijão', 8.60, 'macarrão', 3.60, 'molho de tomate', 17.90,'açucar', 4.30,'chá', 12.65,'creme de leite', 2.89)
print('=' *40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' *40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('=' * 40)