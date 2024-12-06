nome = str(input('\033[0;36mQual é seu nome ?\033[m'))
if nome == 'Ronivaldo':
    print('\033[0;35mQue nome bonito !!!\033[m')
elif nome == 'Maria' or nome == 'Ana' or nome =='José':
    print('\033[33m Seu nome é bem popular no Brasil\033[m')
else:
    print('\033[0;36mSeu nome é bem normal \033[m')
print('\033[0;36mTenha um bom dia,\033[m {}{}{}!'.format('\033[0;32m',nome,'\033[m'))