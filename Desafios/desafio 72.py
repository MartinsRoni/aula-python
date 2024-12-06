#Crie um programa que  tenha uma tupla totalmente preenchida com uma contagem de 0 á 20. Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostralo por extenso.

numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte' )
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break 
    print('Algo errado tente novamente! ', end='')  
print(f'O numero digitado foi o {numeros[num]}')
    


