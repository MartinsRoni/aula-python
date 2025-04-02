#Obs: Dicionários não usam o método APPEND, nele precisamos apenas declarar um elemento

'''dados = dict()
dados = {'nome':'roni','idade':30}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] ='M'# Adicionando um elemento
del dados['idade']# Deletando um elemento do dicionário
print(dados)'''

'''filme = {'titulo':'Star Wars', 
         'ano':1997,
         'diretor':'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')'''

pessoas = {'nome':'Roni','sexo':'M','idade':30}
del pessoas['sexo'] #Deletando um elemento
pessoas['nome'] = 'Leandro' #Alterando valor
pessoas['peso'] = 96.5
for k, v in pessoas.items():# pessoa.items() substitui o Enumerate
    print(f'{k} = {v}')