#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: -Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo do alistamento

#Seu programa também devera mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
ano = int(input('\033[0;34mInsira o ano de seu nascimento:\033'))
if date.today().year - ano  > 18:
    print('\033[0;31mJá se passou {} anos do prazo para você se alistar!\033'.format((atual - ano)-18))
elif date.today().year - ano < 18:
    print('\033[0;33mVocê deve se alistar em {} .Ainda falta {} anos para você se alistar no serviço militar!\033'.format(ano+18, (ano+18)-atual))
else: 
    print('\033[0;32mEstá na hora de você se alistar\033')
