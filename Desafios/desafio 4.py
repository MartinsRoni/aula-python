#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela 

a = input('\033[0;35mDigite algo:\033[m')
print('\033[0;34mO tipo primitivo desse valor é:\033[m',type(a))
print('\033[0;34mSó tem espaços ?\033[m{}{}{}'.format('\033[0;32m', a.isspace(),'\033[m'))
print('\033[0;34mÉ um numero ?\033[m{}{}{}'.format('\033[0;32m',a.isnumeric(),'\033[m'))
print('\033[0;34mÉ alfabético ?\033[m {}{}{}'.format( '\033[0;32m',a.isalpha(),'\033[m'))
print('\033[0;34mÉ alfanumerico ?\033[m{}{}{}'.format('\033[0;32m', a.isalnum(),'\033[m'))
print('\033[0;34mEsta tudo maiusculo ?\033[m{}{}{}'.format('\033[0;32m', a.isupper(),'\033[m'))
print('\033[0;34mEsta todo em minusculo ?\033[m{}{}{}'.format('\033[0;32m', a.islower(),'\033[m'))
