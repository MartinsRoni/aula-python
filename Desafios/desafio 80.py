#Crie um programa que o usuário possa digitar vários valores numericos e cadastreos em uma lista, já na posição correta de inserção sem usar o (Sort()). No final mostre a lista ordenada na tela.

lista = []
for c in range(0,5):
    n = int(input('Digite um valor :'))
    if c == 0 or n > lista[-1]:# lista[-1] para pegar o ultimo numero da lista
            lista.append(n)#Adicionando numero a lista
            print('Adicionado ao final da lista...')  
    else:
          pos = 0
          while pos < len(lista):#Enquanto posição for menor que todos numeros da lista
            if n <= lista[pos]:#Se numero for menor= a valores na lista 
                 lista.insert(pos, n)#Adicionando numero = n na posição = pos
                 print(f'Adicionado na posição {pos} da lista...')
                 break
            pos += 1 #Passando por todos numeros 
print(f'Os valores digitados foram {lista}')            