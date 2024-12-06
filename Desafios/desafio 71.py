# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário qual o valor a ser sacado e o programa ira informar quantas cedulas de cada valor serão entregues.
# Obs: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1

valor = int(input('Qual valor você quer sacar ? '))
total = valor
céd = 50
totalcéd = 0 
while True:
    if total > céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if total == 0:
            break  