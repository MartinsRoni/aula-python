# Crie um programa que leia o nome de uma pessoa e mostre: 
nome = str(input('Digite seu nome:')).strip()
#O  nome com todas as letras maiusculas
print('Seu nome em mausculo é {}'.format(nome.upper()))
#O nome com todas as letras minusculas
print('Seu nome em minusculo é {}'.format(nome.lower()))
#Quantas letras ao todo sem considerar espaços
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#Quantas letras tem o primeiro nome
#print('Seu primeiro nome tem {}'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, e tem {} letras'.format(separa[0], len(separa[0])))

