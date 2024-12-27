# Dicionários

'''filme = {'titulo':'Star Wars',
         'ano': 1997,
         'diretor': 'George Lucas'

}
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')'''

# Prática

'''pessoas = {'nome': 'Roni', 'sexo': 'M', 'idade': 30}
print(pessoas['idade'])
del pessoas['sexo']# Apagando 
pessoas['nome'] = 'Leandro' # Alterando um Value
pessoas['peso'] = 97.5
for k, v in pessoas.items():
    print(f' {k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla']'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())# Dicionários não aceitam [:] cópia mas tem o metodo .copy
for e in brasil:
    '''print(e)'''
    '''for k, v in e.items():
        print(f'O campo {k}, tem valor {v}')'''
    for v in e.values():
        print(v, end=' ')
    print()