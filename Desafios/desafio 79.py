#Crie um programa onde o usuário possa digitar varios valores numericos e cadastre-os em uma lista. Caso o número já exista lá dentro ele não sera adicionado. No final, serão exibidos todos os valores unicos digitados em ordem crescente.
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não foi adicionado')    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ?[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('Finalizado')
        break
valores.sort()
print(f'Os valores digitados foram {valores}')

