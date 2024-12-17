#Ex:1
'''teste = list()
teste.append('Gustavo')
teste.append(40) 

galera = list()
galera.append(teste[:]) 
teste[0] = 'maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

#Ex:2

'''galera = [['João', 20], ['Ravi', 18], ['Maria', 5 ], ['Renan', 16]]
for p in galera:# Para cada pessoa em GALERA
    print(f'{p[0]}, tem {p[1]} anos de idade ')'''

#Ex:3

galera = list()
dados = list()
totmai = totmen = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')))# A lista auxiliar DADOS recebe o input
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])# A lista GALERA recebe uma cópia da lista  auxiliar DADOS
    dados.clear()# Limpa os dados da lista auxiliar DADOS

for p in galera:# Para cada pessoa na lista GALERA
    if p[1] >= 21:# p[1] referencia ao indice 1 que guarda a idade da pessoa
        print(f'{p[0]} É maior de idade!')# p[0] é a referencia ao indice 0 que guarda o nome da pessoa
        totmai += 1 # Contando quantos são maior de idade 
    else:
        print(f'{p[0]} É menor de idade!')
        totmen += 1
print(f'Temos {totmai} maiore de idade e {totmen} menore de idade!')




