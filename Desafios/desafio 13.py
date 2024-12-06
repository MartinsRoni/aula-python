#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento!

salario = int(input('Digite aqui seu salário para saber quanto ficaria com um aumento de 15%: '))

aumento = salario+salario*0.15

print('Seu novo salário com um aumento de 15%, sairia de: R${:.2f}, para: R${:.2f} '.format(salario,aumento))