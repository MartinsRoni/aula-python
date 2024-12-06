#Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

#Calcule o  valor da prestação mensal sabendo que ela nao pode exceder 30% do salario ou então o emprestimo vai ser negado.
import emoji
#vc=ValorCasa
vc = float(input('Informe o valor da casa:'))
#sl=Salario
sl = float(input('Informe sua Renda Mensal:'))
anos = float(input('Informe em quantos anos pretende pagar:'))
meses = anos*12
#pm=Prestação Mensal
pm = vc / meses

if pm >= sl*0.31:
    print('Desculpe, mas seu emprestimo foi negado !')
else:
    print(emoji.emojize('Parabens Imprestimo aprovado!:clapping_hands:'))
