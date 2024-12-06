'''lanche = ['hamburgue','suco','pizza','cookies']
lanche[1] = 'coxinha'#trocar um intem da lista por outro    
lanche.append('goiaba')#Adicionar um item a lista
lanche.insert(0, 'abacaxi')#Inserir um item na posição desejada 
del lanche[2]#Deletar um item da lista recebendo uma chave
lanche.pop()#Deletar o ultimo item da lista, mas pode receber uma chave também
lanche.remove('hamburgue')#Deletar um item também porém não pela chave e sim pelo item
if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)

#valores = list(range(4,11))

valores = [8,2,5,4,9,3,0]#valores desorganizados
valores.sort()#Organizando com Sort
valores.sort(reverse=True)#Organizando de modo inverso
print(valores)

#Praticando 

num = [1,4,0,4,1,9,9,4]
num[1] = 3
num.append(6)
num.sort()
num.insert(3,5)
num.pop(2)
if 5 in num:
    num.remove(5)
print(num)
print(f'Esta lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(4)
valores.append(9)
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

a = [2, 5, 8, 4]
b = a #Desta forma uma lista fica vinculada a outra, toda alteração feita em uma é feita na outra também
b[2] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 5, 8, 4]
b = a[:] #Desta forma é criada uma cópia da lista A assim permitindo a alteração de apeans uma das listas
b[2] = 7
print(f'Lista A: {a}')
print(f'Lista B: {b}')