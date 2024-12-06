#Fatiamento de String

frase = 'curso em video python'
#Fatiamento que vai do indice 9 até o 13 mas sem considerar o ultimo numero
frase[9:13]
#Fatiamento que do primeiro indice vai até o indicado 
frase[:5]
#Fatiamento que seleciona o indicado e pula o quanto for indicado
frase[0:21:2]
#Fatiar até o final da String
frase[15:]
#Fatiar de um determinado ponto ate o final, mas pulando indices
frase[9::3]

#Análize
len(frase)
#Usado para saber quantos indices temos !
frase.count('o')
#usado para contar quantas vezes existe uma determinada letra
frase.count('o',0,13)
#Usado para fazer uma contagem ja com fatiamento
frase.find('deo')
#indica onde uma determinada frase se inicia nos indices
frase.find('Android')
#Se procurarmos por algo que nao existe, ele nos retorna o valor -1
'curso' in frase 
#Saber se existe uma palavra dentro de uma string

#Tranformação 

frase.replace('python','Android')
#trocar uma palavra por outra 

frase.upper()
#trocar para maiusculo todas as letras minusculas 

frase.lower()
#fas o contrarios do metodo upper

frase.capitalize()
#deixa apenas a primeira letra da strind maiuscula e as outras minusculas

frase.title()
#Analiza quantas palavras tem na string verificando pelos espaços e faz um Capitalize em todas as palavras 

frase.strip()
#Remove todos os espaços inuteis no inicio e no fim da string

frase.rstrip()
#Remove somente os espaços do lado direito 

frase.lstrip()
#Remove somente os espaços do lado esquerdo 

#Divisão  (ESTUDAR SPLIT)

frase.split()
#Vai dividir uma string em uma lista, e redefinir cada palavra em um indice novo

#Junção
'-'.join(frase)



