# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média de nota: '))
print(f'O nome do aluno é  {aluno['Nome']}')
print(f'Sua média é de {aluno['Média']}')
if aluno['Média'] < 7.5:
    print('Situação é: Reprovado')
else:
    print('Situação do aluno é: Aprovado')