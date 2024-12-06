#Desenvolva uma logica que leia o peso ea altura de uma pessoa calcule seu IMC e mostre seu status de acordo com a tabela: -Abaixo de 18,5: Abaixo do peso. -Entre 18,5 e 25:Peso Ideal. -25 até 30:Sobrepeso. -30 até 40:Obesidade. -Acima de 40:Obesidade morbida.

peso = float(input('Insira seu peso:'))
altura = float(input('insira sua altura:'))
imc = peso/(altura**2)

if imc<18.5:
    print('Seu IMC é: {:.3} você está Abaixo do Peso'.format(imc))
elif imc<25:
    print('Seu IMC é: {:.3} você esta no peso Ideal'.format(imc))
elif imc<30:
    print('Seu IMC é: {:.3} você esta com Sobrepeso'.format(imc))
elif imc<40:
    print('Seu IMC é: {:.3} você esta com Obesidade'.format(imc))
else:
    print('Seu IMC é: {:.3} você esta com Obesidade Morbida'.format(imc))