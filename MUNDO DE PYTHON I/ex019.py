from random import choice
Aluno1 = input('Qual o nome do aluno: ')
Aluno2 = input('Qual o nome do aluno: ')
Aluno3 = input('Qual o nome do aluno: ')
Aluno4 = input('Qual o nome do aluno: ')
Nomes = [Aluno1, Aluno2, Aluno3, Aluno4]
print('O aluno escolhido foi: {}'.format(choice(Nomes)))