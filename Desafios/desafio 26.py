#Crie um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posiçao ela aparece a primeira vez
#Em que posiçao ela aparece a ultima vez

frase = str(input('Digite a sua frase: ')).upper().strip()
print('Na sua frase a letra "A" aparece {}x'.format(frase.count('A')))
print('Na sua frase a letra "A" se inicia na posição {}'.format(frase.find('A')+1))
print('Na sua frase a posição que está a ultima letra "A" é {}'.format(frase.rfind('A')+1))