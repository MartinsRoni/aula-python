# Crie um programa que leia Nome, Ano de Nascimento e Carteira de Trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário recebera também o ano de contratação e o salário. Calcule e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
cadastro['Idade'] = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - cadastro['Idade']
cadastro['Idade'] = idade
cadastro['Cpts'] = int(input('Carteira de Trabalho(0 não tem): '))
if cadastro['Cpts'] == 0:
    for k, v in cadastro.items():
        print(f'   - {k} tem o valor {v}')
else:
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salario'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (cadastro['Contratação'] + 35) - datetime.now().year
    for k, v in cadastro.items():
        print(f'   - {k} tem o valor {v}')
print(cadastro['Aposentadoria'])