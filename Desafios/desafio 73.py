#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol na ordem de colocação. Depois mostre :
#A) Apenas os 5 primeiros colocados 
#B) Os ultimos 4 colocados da tabela 
#C) Uma lista com os time em ordem alfabetica
#D) Em que posição esta o time da chapecoense.

tabela = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo','Bragantino','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco da Gama','Bahia','Santos','Goias','Coritiba','América-MG')
print('')
print(f'Lista de times do Brasileirão: ',tabela)
print('=-'*15)
print(f'Os 5 primeiros colocados são:',tabela[0:5])
print('=-'*15)
print(f'Os ultimos 4 colacados são: ',tabela[-4:])
print('=-'*15)
print(f'Os times em ordem alfabética são estes: ',sorted(tabela))
print('=-'*15)
print(f'E o time do Cuiaba está na {tabela.index('Cuiabá')}º posição')