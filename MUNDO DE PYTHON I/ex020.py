from random import shuffle
Aluno1 = str(input('Qual o nome do aluno: '))
Aluno2 = str(input('Qual o nome do aluno: '))
Aluno3 = str(input('Qual o nome do aluno: '))
Aluno4 = str(input('Qual o nome do aluno: '))
print('A ordem dos nome colocados são \n{}, {}, {}, {}.' .format(Aluno1, Aluno2, Aluno3, Aluno4))
lista = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle(lista)
print('A nova ordem é: {}'.format(', '.join(lista)))