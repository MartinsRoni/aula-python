#Crie um programa que leia o nome e sexo de várias pessoas. A cada pessoa identificada o programa devera perguntar se o usuário quer ou não continuar. No final mostrar :
#Quantas pessoas tem mais de 18 anos 
#Quantos homens foram cadastrados 
#Quantas mulheres tem menos de 20 anos 
totalpessoa_mais18 = 0
totalhomem = 0
totalmulher_menos20 = 0



while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        totalpessoa_mais18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
        if sexo in 'M':
            totalhomem += 1
        elif sexo in 'F' and idade < 20:
            totalmulher_menos20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        print('Acabou')
        break
print(f'Programa finalizado! \nTotal de pessoas com mais de 18 anos: {totalpessoa_mais18} \nTivemos {totalhomem} homens na pesquisa. \nE temos {totalmulher_menos20} mulheres com menos de 20 anos.')