numero_1 = int(input('Digite seu primeiro numero para soma:'))
numero_2 = int(input('Digite seu segundo numero para soma:'))
            
soma =  numero_1 + numero_2 
#Jeito convencional 
#print ('A soma dos numeros', numero_1, 'e', numero_2 , ' é:', soma)

#Jeito mais pratico de escrever o codigo usando chaves e .format()

print(' soma de {}{}{} mais {}{}{} equivale a : {}{}{}'.format('\033[0;34m',numero_1,'\033[m', '\033[0;34m', numero_2, '\033[m', '\033[0;34m',soma, '\033[m'))