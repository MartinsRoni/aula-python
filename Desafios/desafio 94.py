# Crie um programa que leia Nome, Sexo e Idade de várias pessoas, guardando os dados de cada pessoas em um dicionário e todos os dicionários em uma lista. No final mostre: A) Quantas pessoas foram cadastradas B) A média de idade do grupo C) Uma lista com todas as mulheres D) Uma lista com todas as pessoas com idade acima da média.
pessoas = list()
cad = dict()
soma = media = 0
while True:
    cad.clear()
    cad['nome'] = str(input('Nome: '))
    while True:
        cad['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if cad['sexo'] in 'MF':
            break
        print('Por favor digite somente M ou F.')
    cad['idade'] = int(input('Idade: '))
    soma += cad['idade']
    pessoas.append(cad.copy())   
    while True:
        res = str(input('Deseja continuar[S/N]: ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO. Digite somente S ou N')
    if res == 'N':
        break
print('-='*30)
print(f'A) Foram cadastradas {len(pessoas)} pessoas na lista.')
media = soma / len(pessoas)
print(f'B) A média de idade do grupo é de {media:.2f} anos')
print('C) As mulheres cadastradas foram', end='' )
for p in pessoas:#Para cada pessoa na lista Pessoas
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]} ', end='')
print()
print('D) As pessoas com idade acima da média do grupo são ', end='' )
for p in pessoas:
    if p['idade'] > media:
        print(f'  {p["nome"]}', end='')
print()
