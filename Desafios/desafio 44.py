#Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal e condição de pagamento: 
#-A vista dinheiro/cheque: 10% de desconto
#-A vista no cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros

print('='*5,'Loja Martins','='*5)
valor = int(input('Insira o valor da compra: R$ '))
print('''
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Selecione a sua opção: '))

if opcao == 1:
    print('Sua compra no valor de R${} à vista no dinheiro ou cheque vai custar R${:.0f}'.format(valor, valor - valor*0.10))
elif opcao == 2:
    print('Sua compra no valor de R${} à vista no cartão vai custar R${:.0f}'.format(valor,valor - valor*0.05))
elif opcao == 3:
    print('Sua compra no valor de R${} em até 2x no cartão vai custar R${}'.format(valor, valor))
elif opcao == 4: 
    totparc = int(input('Quantas parcelas?'))
    parcela = (valor+valor*0.20)/totparc
    print('Sua compra no valor de R${},00 vai ser parcelada em {}X e vai ficar {}X de R${:.0f},00'.format(valor, totparc,totparc, parcela))
else:
    print('OPÇÃO INVALIDA TENTE NOVAMENTE!')