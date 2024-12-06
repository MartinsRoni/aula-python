#Crie um programa que leia duas notas de um aluno e calcule sua media mostrando uma mensagem no final de acordo com a media atingida: - media abaixo de 5,0: REPROVADO. - media entre 5,0 e 6,9: RECUPERAÇÃO. - Media 7,0 ou superior: APROVADO

nota1 = float(input('\033[0;34mInsira sua primeira nota:\033[m'))
nota2 = float(input('\033[0;34mInsira sua segunda nota:\033[m'))
media = (nota1+nota2)/2

if media <= 4:
    print('\033[0;31mVOCÊ ESTÁ REPROVADO\033[m')
elif media <= 6.9:
    print('\033[0;33mVOCÊ FICOU EM RECUPERAÇÃO\033[m')
else:
    print('\033[0;32mPARABÉNS VOCÊ ESTÁ APROVADO\033[m')


