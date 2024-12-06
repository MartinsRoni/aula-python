#ceil arredonda para cima 
#floor arredonda para baixo
#trunc para trucar um numero
#pow 
#sqrt calcular raiz quadrada
#factorial para calculo de fatorial

# Para importar um modulo completo -> (import math)

#Para importar uma função especifica do modulo -> (from math import sqrt)

from math import sqrt, floor
#Apertando (Ctrl + espaço ), aparece todas as opções !
num = int(input('Digite um numero:'))

raiz = sqrt(num)
print('A raiz quadrada de {}, é igual a {}'.format(num, floor(raiz)))

# utilizando o modulo random 
import random

num = random.randint(1,10)
print(num)
# utilizando o modulo emoji
import emoji 
print(emoji.emojize('I Love You :red_heart:'))