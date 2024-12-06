#Faça um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento.      Para salarios superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais um aumento de 15%                

salario = float(input('Insira o valor do seu salário para saber seu aumento:'))
aumento1 = salario*0.10 + salario
aumento2 = salario*0.15 + salario

if salario <= 1250:
    print('Parabens você teve um aumento de 15% do seu salário, passando a receber R${:.2f} '.format(aumento2))
else:
    print('Parabens voce teve um aumento de 10% do seu salario, passando a receber R${:.2f}'.format(aumento1))