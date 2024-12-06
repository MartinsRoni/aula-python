#Crie um programa onde um usuário digite uma expressão qualquer que use parenteses. Seu aplicativo devera analizar se a expressão passada esta com os parenteses abertos e fechados na ordem correta.

expre = str(input('Digite a Expressão:'))
pilha = []

for símb in expre:
    if símb ==  '(':
        pilha.append('(')#Adicionando na pilha
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()#Removendo da pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão correta')
else:
    print('Expressão incorreta')