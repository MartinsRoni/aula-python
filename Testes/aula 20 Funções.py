#Ex 1
'''def soma(a ,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A = B = {s}')


soma(b=10, a=3)
soma(5, 3)'''

#Ex 2
# Empacotamento
'''def contador(* num):# O (* desempacotar) o asterisco coloca tudo que foi recebudi dentro da referencia citada 
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim')


contador(5, 3, 8, 6, 10, 46)
contador(15, 28, 137)'''

#Ex 3
'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} que ao todo são {tam} números')


contador(5, 3, 8, 6, 10, 46)
contador(15, 28, 137)'''

#Ex 4 Desempacotamento 1º tec
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1


valores = [8, 77, 15, 2, 33]
dobra(valores )
print(valores)'''

#Ex 5 Desempacotamento 2º tec
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(6, 9)
soma(7, 4, 3)
