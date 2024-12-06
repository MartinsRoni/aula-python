'''carro.siga()
if carro.esquerda():

 carro.siga()
 carro.direita()
 carro.siga()
 carro.direita()
 carro.esquerda()
 carro.siga()
 carro.direita()
 carro.siga()
 
else

 carro.siga()
 carro.esquerda()
 carro.siga()
 carro.esquerda()
 carro.siga()
carro.pare()'''

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Carro Novo')
else:
    print('Carro velho')
print('--Fim--')

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1+n2)/2
print('A sua média foi {:.2}'.format(m))
if m >= 7:
    print('Parabens!!!, Voçe foi bem nos seus estudos')
else:
    print('Que pena, parece que voçe precisa estudar mais =(')
